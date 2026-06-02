'''
RefNode and RefTree classes for organizing the parsed information into a digestible tree.
'''

from src.ref_splitter import RefEntry

class RefTree:
    '''manages the tree of reference nodes
    and supports exporting files in various formats'''
    _instance = None

    nodes: list[RefNode] = []
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        else:
            raise ValueError("RefTree Singleton already created")
        return cls._instance
    
    def __init__(self) -> None:
        print("RefTree created")
    
    def append(self, node: RefNode) -> None:
        self.nodes.append(node)
    
    def add_new_node(self, entry: RefEntry) -> RefNode:
        new_node = RefNode(entry)
        
        return new_node

class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry
    
    def __init__(self, entry) -> None:
        self.entry = entry
        self.id = 0