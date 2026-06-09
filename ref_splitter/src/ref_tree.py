'''
RefNode and RefTree classes for organizing the parsed information into a digestible tree.
'''

from src.ref_splitter import RefEntry


class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    parent_id: int
    entry: RefEntry
    
    def __init__(self, entry, this_id: int, parent_id: int) -> None:
        self.entry = entry
        self.id = this_id
        self.parent_id = parent_id

class RefTree:
    '''Manages the tree of reference nodes
    The structure of this tree will denote the organization and pathing of pages when exported'''
    _instance = None

    nodes: list[RefNode] = []
    links: dict[str, str] # format is: link_text : link_path
    
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
        #TODO: Properly organize the tree nodes into the correct hierarchy
        new_node = RefNode(entry, len(self.nodes), 0)
        return new_node