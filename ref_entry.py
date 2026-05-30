class RefEntry:
    '''A single reference entry (page)'''
    title: str
    content: str

    def __init__(self, title:str, content:str):
        self.title = title
        self.content = content
        print(f"New entrty: {title}, {content}")
        
class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry

class RefTree:
    '''Singleton managing the tree of reference nodes'''
    nodes: list[RefNode] = []