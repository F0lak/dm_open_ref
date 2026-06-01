'''
Ref Splitter class.
The Ref Splitter takes in a string given by the file i/o module and processes it into a RefTree
'''
from bs4 import BeautifulSoup, Tag
from ref_entry import RefEntry

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
    pretty_soup: str

    def __init__(self, doc_str: str):
        print("new ref splitter")
        self.soup = BeautifulSoup(doc_str, "lxml")
        self.pretty_soup = self.soup.prettify()

    def save_pretty_soup(self):
        '''
        saves the pretty soup to a text file
        useful for reading through and seeing what we're working with
        '''
        with open("pretty_soup.txt", "w", encoding="utf-8") as file:
            file.write(self.pretty_soup)

    def print_pages(self, length: int):
        '''
        prints up to 'length' pages from the soup
        '''

        pages = self.soup.find_all('a', attrs={"name":True}, limit = length)
        for i, page in enumerate(pages):
            content_text: str = page.get_text(separator = '\n', strip = True)
            print(f"{i}:\n\t{content_text}")

    def save_pages(self, length: int):
        '''
        Saves each page that is found
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

    def build_ref_entries(self, length: int):
        '''
        Builds Ref Entries for each page found in the soup
        '''
        pages = self.soup.find_all('a', attrs={"name":True}, limit = length)

        for i, page in enumerate(pages):
            content_text: str = page.get_text(separator = '\n', strip = True)
            entry = RefEntry(str(page.attrs["name"]), content_text)
            print(f"Built entry for page {i}: {entry.id}: {entry.title}, {entry.ref_path}")
            entry.relative_paths = self.extract_related_entries(page)
            self.save_entry(entry)

    def extract_related_entries(self, page: Tag) -> list[str]:
        '''
        extracts the list of related entries
        '''
        relatives: list[str] = []
        rel_list = page.find('dl')

        if rel_list:
            for relative in rel_list.find_all('dd'):
                rel_a = relative.find('a', attrs={"href":True})
                if rel_a is not None:
                    rel_path = str(rel_a.attrs["href"])
                    if rel_path:
                        relatives.append(rel_path[1:])

        print(relatives)
        return relatives
