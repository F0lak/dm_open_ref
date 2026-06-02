'''
Ref Splitter class.
The Ref Splitter takes in a string given by the file i/o module and processes it into a RefTree
'''
from bs4 import BeautifulSoup, Tag
from pprint import pprint

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
    ref_id: str # the name of the RefEntry as found in the DM reference <a> tag
    content: list[str] # A list of content delimited by <p> tags
    title: str # The page title of the entry
    ref_path: list[str] # The path to the path of this page in the original DM referene
    desc_lists: dict[str, list[str]] # A dictionary of formatted lists found in the page

    def __init__(self, entry_id:str):
        self.ref_id = entry_id
        self.content = []
        
        self.related_links = {}
        self.page_links = {}

        self.set_ref_path()
        self.set_title()

    def set_ref_path(self) -> None:
        '''Uses the ref_id to populate the ref_path list where each
        consecutive element is the next branch on the DM Reference's node tree'''
        self.ref_path = self.ref_id.split('/')
        self.ref_path.pop(0)

    def set_title(self) -> None:
        '''Sets the entry title to the final entry in the ref_path list'''
        self.title = self.ref_path[-1]

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

    soup: BeautifulSoup
    entries: list[RefEntry]
    pages: list[str]
    links: dict[str, str]
    elems_to_remove: list[Tag]
    
    INLINE_TAGS: dict[str, str] = {
        "b" : "BOLD",
        "i" : "ITALIC",
        "u" : "UNDERLINE",
        "tt" : "CODE",
        "var" : "CODE"
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
            desc_lists = self.extract_description_lists(page)
            self.purge_elements()

            entry = RefEntry(str(page.attrs["name"]))

            content = self.extract_content(page)
            entry.content = content
            entry.desc_lists = desc_lists

            self.entries.append(entry)
            self.pages.append('\n\n'.join(content))

            pprint(entry.desc_lists)
            
    def extract_content(self, page: Tag) -> list[str]:
        '''
        Extracts all of the content contained within <p> tags,
        converts common tags (<tt>, <b>, <i>) to tokens
        and formats it into a single string.
        
        Returns a list of paragraphs coresponding to <p> tags and
        code blocks coresponding to xmp tags
        '''
        content_list: list[str] = []
        content = page.find_all(['p', 'xmp'])
        for tag in content:
            match tag.name:
                case 'p':
                    raw_text = str(tag)
                    tokenized_text = self.tokenize(raw_text)
                    clean_text = self.clean_paragraph(tokenized_text)
                    if clean_text:
                        content_list.append(clean_text)
                case 'xmp':
                    content_list.append(f'[CODEBLOCK]{tag.get_text()}[/CODEBLOCK]')
            
        return content_list
    
    def tokenize(self, text: str) -> str:
        '''
        converts inline html tags as declared in INLINE_TAGS
        to their tokenized counterpart
        '''
        for tag, token in self.INLINE_TAGS.items():
            text = text.replace(f'<{tag}>', f'[{token}]')
            text = text.replace(f'</{tag}>', f'[/{token}]')
        return text

    def clean_paragraph(self, text: str) -> str:
        '''
        checks for malformed tags and breaks the paragraph into a
        single string with no newlines or additional formatting
        '''
        if not text.startswith("<p>"):
            raise ValueError("Expected tag to open with <p>")
        if not text.endswith("</p>"):
            raise ValueError("Expected tag to close with </p>")
        
        text = text[3:-4]
        words = text.split()
        return " ".join(words)

    def extract_description_lists(self, page: Tag) -> dict[str, list[str]]:
        '''
        Finds all of the description lists in the entry and returns them in a dictionary
        where key = list title, value = list entries

        Not 100% sure this will be enough for the lists that the DM reference populates, but here we are...    
        '''

        final_desc_lists: dict[str, list[str]] = {}

        lists = page.find_all('dl')

        # Normally I don't like using tiny var names, but these ones corespond to the html tags
        if(lists):
            for dl_tag in lists:
                # the dm reference entries, thankfully have a standard format for these lists.
                # dt is consistently used for the name of the list, and dd for the entries in it.
                dt_tag: Tag | None  = dl_tag.find('dt')
                if dt_tag:
                    term_string: str = dt_tag.get_text(strip=True)
                    if term_string in final_desc_lists:
                        raise ValueError(f"Term '{term_string}' is being declared more than once for this page")

                    details: list[str] = []
                    # Unfortunately, the composition of the tags in these desc lists is a thing that one would not wish to behold
                    # So we have to 
                    for dd_tag in dl_tag.find_all('dd'):
                        dd_text = "".join(dd_tag.find_all(string=True, recursive=False)).strip()
                        a_tag = dd_tag.find('a', attrs={"href":True}, recursive=False)
                        if a_tag is not None:
                            link_path = self.encode_link(a_tag)
                            dd_text += f"[LINK]{link_path}[/LINK]"
                        details.append(dd_text)

                    if len(details) == 0:
                        raise ValueError("List has no details")

                    final_desc_lists[term_string] = details

                else:
                    raise ValueError("Malformed Declaration List in Reference")

                # strip it here, since we don't want it in our content
                self.elems_to_remove.append(dl_tag)

            print("Lists found!\n\n")

        return final_desc_lists

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
