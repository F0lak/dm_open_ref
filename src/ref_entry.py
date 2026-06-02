

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
    content: str # the content of the entry, not including the See Also links
    title: str # The page title of the entry
    ref_path: list[str] # The path to the path of this page in the original DM referene
    desc_lists: dict[str, list[str]] # A dictionary of formatted lists found in the page

    def __init__(self, entry_id:str, content:str):
        self.ref_id = entry_id
        self.content = content
        
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

class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry

class RefTree:
    '''Singleton managing the tree of reference nodes'''
    nodes: list[RefNode] = []
