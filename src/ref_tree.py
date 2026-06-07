'''
RefNode and RefTree classes for organizing the parsed information into a digestible tree.
'''

from src.ref_splitter import RefEntry


class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry
    
    def __init__(self, entry, id: int) -> None:
        self.entry = entry
        self.id = id

class RefTree:
    '''manages the tree of reference nodes'''
    _instance = None

    nodes: list[RefNode] = []
    links: dict[str, str]
    
    def __init__(self) -> None:
        print("RefTree created")
        
    def build_tree_from_entries(self, entries: list[RefEntry], links: dict[str, str]) -> None:
        for entry in entries:
            new_node = self.create_node(entry)
            self.append(new_node)
            
        self.links = links
            
        print(f"RefTree built with {len(self.nodes)} nodes")
            
    def append(self, node: RefNode) -> None:
        self.nodes.append(node)
    
    def create_node(self, entry: RefEntry) -> RefNode:
        new_node = RefNode(entry, len(self.nodes))
        return new_node