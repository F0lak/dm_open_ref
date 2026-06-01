class RefEntry:
    '''A single reference entry (page)'''
    id: str
    content: str
    title: str
    parent_id: str
    ref_path: str
    relative_paths: list[str] = []

    def __init__(self, entry_id:str, content:str):
        self.id = entry_id
        self.content = content

        #print(f"New entrty: {title}")
        path = entry_id.split('/')
        self.title = path[-1]
        path.pop()
        self.ref_path = "/".join(path)

class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry

class RefTree:
    '''Singleton managing the tree of reference nodes'''
    nodes: list[RefNode] = []
