'''
Ref Splitter class.
The Ref Splitter takes in a string given by the file i/o module and processes it into a RefTree
'''
from bs4 import BeautifulSoup, Tag
from src.ref_entry import RefEntry
from pprint import pprint

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
    
    def __init__(self, doc_str: str):
        print("new ref splitter")
        self.soup = BeautifulSoup(doc_str, "lxml")

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

    def save_pages(self, length: int | None):
        '''
        Saves each page that is found
        length is optional number of pages
        '''

        pages = self.soup.find_all('a', attrs={"name":True}, limit = length)

        for i, page in enumerate(pages):
            content_text: str = page.get_text(separator = '\n', strip = True)
            with open(f"pages/{i}.txt", "w", encoding="utf-8") as file:
                file.write(content_text)

    def save_entry(self, entry: RefEntry):
        '''
        Saves a Ref Entry to a text file
        '''
        with open(f"entries/{entry.title}.txt", "w", encoding="utf-8") as file:
            file.write(entry.content)

    def build_ref_entries(self, length: int | None = None):
        '''
        Builds Ref Entries for each page found in the soup
        'length' is an optional parameter to limit the number of pages built
        '''
        pages = self.soup.find_all('a', attrs={"name":True}, limit = length or None)

        for i, page in enumerate(pages):
            see_also_links = self.extract_related_entries(page)
            
            content_text: str = page.get_text(separator = '\n', strip = True)
            entry = RefEntry(str(page.attrs["name"]), content_text)
            
            entry.related_links = see_also_links
            
            print(f"Built entry for page {i}: {entry.ref_id}: {entry.title}, {entry.ref_path}\n\n\n")
            self.save_entry(entry)
            
            entry.desc_lists = self.extract_description_lists(page)
            pprint(entry.desc_lists)

    def extract_related_entries(self, page: Tag) -> dict[str, str]:
        '''
        Converts the links in the "See Also" section into a dictionary
        and removes them from the Soup Page
        '''
        relatives: dict[str, str] = {}
        rel_list = page.find('dl')

        if rel_list:
            for relative in rel_list.find_all('dd'):
                rel_a = relative.find('a', attrs={"href":True})
                if rel_a is not None:
                    rel_path = str(rel_a.attrs["href"])
                    if rel_path:
                        relatives[rel_a.get_text(strip=True)] = rel_path[1:]

            rel_list.decompose()

        print(relatives)
        return relatives
    
    def extract_description_lists(self, page: Tag) -> dict[str, list[str]]:
        '''
        ok, so we'll have a few different desc lists showing up in the documents.
        The common ones are the See Also links, Format, and Arguments and return value.
        
        I need to write a function that finds all of the desclists in the document, and pops them into a dictionary of lists,
        where the key of each entry is the name of the list
        and the value is a dictionary of the values of the list.
        
        Some values can be links, like in See Also.  Sometimes it's something like an argument, and an argument description.
        '''
        
        final_desc_lists: dict[str, list[str]] = {}
        
        lists = page.find_all('dl')
        
        # Normally I don't like using tiny var names, but these ones corespond to the html tags
        if(lists):
            for dl_tag in lists:
                # the dm reference entries, thankfully have a standard format for these lists.
                # dt is consistently used for the name of the list, and dd for the entries in it.
                dt_tag: Tag | None  = dl_tag.find('dt')
                if(dt_tag):
                    term_string: str = dt_tag.get_text(strip=True)
                    if(term_string in final_desc_lists):
                        raise ValueError("Term '{term_string}' is being declared more than once for this page")
                    
                    details: list[str] = []
                    # Unfortunately, the composition of the tags in these desc lists is a thing that one would not wish to behold
                    # So we have to 
                    for dd_tag in dl_tag.find_all('dd'):
                        dd_text = "".join(dd_tag.find_all(string=True, recursive=False)).strip()
                        details.append(dd_text)
                    
                    if(len(details) == 0):
                        raise ValueError("List has no details")
                    
                    final_desc_lists[term_string] = details
                    
                else:
                    raise ValueError("Malformed Declaration List in Reference")
            print("Lists found!\n\n")
        
        return final_desc_lists
        
