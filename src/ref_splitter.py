'''
Ref Splitter class.
The Ref Splitter takes in a string given by the file i/o module and processes it into a RefTree
'''
from bs4 import BeautifulSoup, Tag
import warnings
from src.token_table import INLINE_TOKEN_TABLE


class RefEntry:
    '''
    An intermediate representation of a single page entry from the DM reference
    providing a standardized format that can be used in different formatting methods
    (ie: Official DM Reference, dm_open_ref)
    It holds members related to important data extracted from the reference, such as
        - Page content
        - Related Pages (extracted from "See Also")
        - Links within the page contents
    '''

    def __init__(self, eid: str):
        self.ref_id = "NO_ID" # the name of the RefEntry as found in the DM reference <a> tag (ie: /client/proc/New())
        self.content = [] # A list of content delimited by <p> tags
        self.title: str = "" # The title for the reference entry, derived from ref_id
        self.ref_path: list[str] = [] # The path to this page in the original DM referene
        self.entry_type: str # the type of entry this is: "Info", "Proc", "Var", "Object"
        
        self.related_links = {}
        self.page_links = {}
        
        # Standard DM Reference fields
        self.see_also: list[str] = [] # links to related pages
        # proc-only fields
        self.format: list[str] = []     # the format that the proc takes
        self.returns: list[str] = []    # return value of the proc
        self.args: list[str] = []       # arguments of the proc
        self.when: list[str] = []       # when the proc is normally invoked
        self.default_action: list[str] = [] # default behaviour
        # var-only fields
        self.default_value: list[str] = [] # variable default value

        self.ref_id = eid
        self.set_ref_path()
        self.set_title()
        self.entry_type = self.set_ref_entry_type()
        
    def set_title(self) -> None:
        '''Sets the title based on the path'''
        print(self.ref_path)
        title_index = len(self.ref_path) - 1
        if title_index >= 0:
            self.title = self.ref_path[title_index]
        else:
            self.title = "[NO_TITLE]"

    def set_ref_path(self) -> None:
        '''Uses the ref_id to populate the ref_path list where each
        consecutive element is the next branch on the DM Reference's node tree'''
        self.ref_path = self.ref_id.split('/')
        self.ref_path.pop(0)
        
    def set_ref_entry_type(self) -> str:
        '''sets the entry type based on the ref_path'''
        # TODO add in "Object" for byond built-in object types (datum, atom, client, etc.)
        
        if "var" in self.ref_path:
            return "var"
        if "proc" in self.ref_path:
            return "proc"
        return "info"

    def get_path(self) -> str:
        '''Returns ref_path rebuilt into a string in the format "/a/b/c"'''
        return '/'.join(self.ref_path)

class RefSplitter:
    '''
    Scans through the file, identifying individual reference entries
    For each entry, it performs the following steps:
    extracts the entry's information
    strips away formatting
    creates and populates a Ref Entry with the relevant information
    Creates a Ref Node using the Ref Entry
    Finally, adds the RefNode to the RefTree and assigns its parent
    '''
        
    # For mapping dt tags to field attributes
    field_mapping = {
        "Format:": "format",
        "Returns:": "returns",
        "See also:": "see_also",
        "Args:": "args",
        "When:": "when",
        "Default action:": "default_action",
        "Default value:": "default_value",
        }

    def __init__(self, doc_str: str):
        print("new ref splitter")
        self.soup = BeautifulSoup(doc_str, "lxml")
        self.entries = []
        self.pages = []
        self.links = {}
        self.elems_to_remove = []

    def save_pretty_soup(self):
        '''
        saves the pretty soup to a text file
        useful for reading through and seeing what we're working with
        '''
        with open("pretty_soup.txt", "w", encoding="utf-8") as file:
            file.write(self.soup.prettify())

    def print_pages(self, length: int):
        '''
        prints up to 'length' pages from the soup
        '''
        pages = self.soup.find_all('a', attrs={"name":True}, limit = length)
        for i, page in enumerate(pages):
            content_text: str = page.get_text(separator = '\n', strip = True)
            print(f"{i}:\n\t{content_text}")

    def save_pages(self):
        '''
        Saves all of the pages that have been parsed
        '''
        for i, page in enumerate(self.pages):
            with open(f"pages/{i}.txt", "w", encoding="utf-8") as file:
                file.write(page)

    def save_entry(self, entry: RefEntry):
        '''
        Saves a Ref Entry to a text file
        '''
        content: str = "\n\n".join(entry.content)
        with open(f"entries/{entry.title}.txt", "w", encoding="utf-8") as file:
            file.write(content)
            
    def purge_elements(self) -> None:
        for tag in self.elems_to_remove:
            tag.decompose()

    def build_ref_entries(self, length: int | None = None):
        '''
        Builds Ref Entries for each page found in the soup
        'length' is an optional parameter to limit the number of pages built
        '''
        for page in self.soup.find_all('a', attrs={"name":True}, limit = length or None):
            entry_id: str = str(page.attrs["name"])
            print(f'Parsing Page: {entry_id}')
            
            desc_lists = self.format_description_lists(page)
            self.purge_elements()

            entry = RefEntry(entry_id)

            content = self.extract_content(page)
            entry.content = content
            self.set_common_fields(entry, desc_lists)

            self.entries.append(entry)
            self.pages.append('\n\n'.join(content))

            #pprint(entry.desc_lists)
            
    def set_common_fields(self, entry: RefEntry, desc_lists: dict[str, list[str]]) -> None:
        for field, content in desc_lists.items():
            if attr_name := self.field_mapping.get(field):
                if not hasattr(entry, attr_name):
                    raise AttributeError(f'{attr_name} is not declared on RefEntry')
                setattr(entry, attr_name, content)
            
    def extract_content(self, page: Tag) -> list[str]:
        '''
        Extracts all of the content contained within <p> tags,
        converts common tags (<tt>, <b>, <i>) to tokens
        and formats the content into a single string.
        
        Returns the content as a list containing:
            paragraphs coresponding to <p> tags
            code blocks coresponding to xmp tags
            description lists (that are not common fields)
        '''
        if page is None:
            raise ValueError("Cannot extract content from non-existant page")
        
        content = page.find_all(['p', 'xmp'])
        if len(content) == 0:
            raise ValueError("Page has no Content")
        
        content_list: list[str] = []
        for tag in content:
            match tag.name:
                case 'p':
                    #TODO handle p classes to tokenize them, allowing markdown and html to rebuild them properly
                    raw_text = str(tag)
                    clean_text = self.clean_paragraph(raw_text)
                    tokenized_text = self.tokenize(clean_text)
                    if tokenized_text:
                        tokenized_text = self.tokenize_paragraph(tokenized_text, tag)
                        content_list.append(tokenized_text)
                # xmp is handled here to properly tokenize the codeblocks.
                # using the standard tokenizer will destroy the text inside the code block
                case 'xmp':
                    content_list.append(f'[CODEBLOCK]{tag.get_text()}[/CODEBLOCK]')
                case 'dl':
                    content_list.append(self.tokenize(str(tag)))
            
        return content_list
    
    def tokenize(self, text: str) -> str:
        '''
        converts inline html tags as declared in INLINE_TAGS
        to their tokenized counterpart
        '''
        for row in INLINE_TOKEN_TABLE:
            html_tag = row["html"]
            token = row["TOKEN"]
            text = text.replace(f'<{html_tag}>', f'[{token}]')
            text = text.replace(f'</{html_tag}>', f'[/{token}]')
        return text
    
    def tokenize_paragraph(self, paragraph: str, tag: Tag) -> str:
        '''Tokenizes a paragraph block based on its class attribute'''
        if p_classes := tag.get('class'):
            print(f'paragraph classes = {p_classes}')
            if 'compatibility' in p_classes:
                paragraph = f'[P_COMPATABILITY]{paragraph}[/P_COMPATABILITY]'
            elif 'performance' in p_classes:
                paragraph = f'[P_PERFORMANCE]{paragraph}[/P_PERFORMANCE]'
            elif 'note' in p_classes:
                paragraph = f'[P_NOTE]{paragraph}[/P_NOTE]'
            elif 'tip' in p_classes:
                paragraph = f'[P_TIP]{paragraph}[/P_TIP]'
            elif 'deprecated' in p_classes:
                paragraph = f'[P_DEPRECTATED]{paragraph}[/P_DEPRECATED]'
            elif 'didyouknow' in p_classes:
                paragraph = f'[P_DIDYOUKNOW]{paragraph}[/P_DIDYOUKNOW]'
            elif 'security' in p_classes:
                paragraph = f'[P_SECURITY]{paragraph}[/P_SECURITY]'
                
        return paragraph

    def clean_paragraph(self, text: str) -> str:
        '''
        checks for malformed tags and breaks the paragraph into a
        single string with no newlines or additional formatting
        '''
        if not text.startswith("<p"):
            raise ValueError(f"Expected tag to open with <p>. Source Text:\n{text}")
        if not text.endswith("</p>"):
            raise ValueError(f"Expected tag to close with </p>. Source Text:\n{text}")
        
        open_tag_terminator_index = text.find('>')
        
        if open_tag_terminator_index == 0:
            raise ValueError("open tag is never terminated.")
        
        text = text[open_tag_terminator_index+1:-4]
        words = text.split()
        return " ".join(words)

    def format_description_lists(self, page: Tag) -> dict[str, list[str]]:
        '''
        parses description lists and extracts common fields  
        '''
        common_fields: dict[str, list[str]] = {}

        lists = page.find_all('dl')

        if(lists):
            for dl_tag in lists:
                # the dm reference entries, thankfully have a standard format for these lists.
                # dt is consistently used for the name of the list, and dd for the entries in it.
                
                # DM Ref only ever has one term per list, so there's no need to parse more than one.
                # this would need to be changed when the standard for the html ref is modernized
                term_string = self.get_term_string(dl_tag)
                
                details: list[str] = []
                # Unfortunately, the composition of the tags in these desc lists is a thing that one would not wish to behold
                # So we have to be very careful here.
                for dd_tag in dl_tag.find_all('dd'):
                    dd_text = "".join(dd_tag.find_all(string=True, recursive=False)).strip()
                    a_tag = dd_tag.find('a', attrs={"href":True}, recursive=False)
                    if a_tag is not None:
                        link_path = self.encode_link(a_tag)
                        dd_text += f"[LINK]{link_path}[/LINK]"
                    details.append(dd_text)

                if len(details) == 0:
                    warnings.warn(f"Term '{term_string}' is being declared more than once for this page.  They will be combined",
                        UserWarning)
                    details.append("EMPTY")

                if term_string in common_fields:
                    warnings.warn(f"Term '{term_string}' is being declared more than once for this page.  They will be combined",
                        UserWarning)
                    common_fields[term_string].extend(details)
                
                common_fields[term_string] = details
                self.elems_to_remove.append(dl_tag)

        return common_fields
        
    def get_term_string(self, dl_tag: Tag) -> str:
        if dt_tag := dl_tag.find('dt'):
            term_string: str = dt_tag.get_text(strip=True)
        else:
            term_string: str = "UNKNOWN_TERM"
            warnings.warn("Expected a description term, but none was provided.  Adding Placeholder",
                UserWarning)
        return term_string

    def encode_link(self, a_tag: Tag | None) -> str:
        '''
        Encodes a hyperlink from an <a> tag into the links dictionary.
        '''
        if a_tag is None:
            raise TypeError("a Tag is 'None'")
        if a_tag.name != 'a':
            raise RuntimeError(f"Trying to encode an invalid tag ({a_tag.name}).  Expected 'a'")
        if "href" not in a_tag.attrs:
            raise ValueError("a Tag does not have href attribute")
            
        link_path = str(a_tag.attrs["href"])
        link_path = link_path[1:] # strip out the # at the beginning of the paths
        if len(link_path) == 0:
            raise ValueError("Empty link path")
        
        link_text = a_tag.get_text(strip=True)
        if len(link_text) == 0:
            link_text = link_path

        self.links[link_path] = link_text
        return link_path
