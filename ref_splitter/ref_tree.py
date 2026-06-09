'''
RefNode and RefTree classes for organizing the parsed information into a digestible tree.
'''

from .ref_splitter import RefEntry

class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    def __init__(self, entry: RefEntry) -> None:
        self.entry: RefEntry = entry
        self.is_index: bool = False

class RefTree:
    '''Manages the tree of reference nodes
    The structure of this tree will denote the organization and pathing of pages when exported'''
    _instance = None

    nodes: list[RefNode] = []
    links: dict[str, str] # format is: link_text : link_path
    
    def __init__(self) -> None:
        print("RefTree created")
        
    def build_tree_from_entries(self, entries: list[RefEntry], links: dict[str, str]) -> None:
        
        self.links = links
        tree_map: dict[str, int] = {}
        
        # populate the tree with entries
        for entry in entries:
            tree_map[entry.ref_id] = entry.pid
            self.nodes.append(RefNode(entry))
        
        # check for index entries (pages that share a path with a directory)
        for idx, entry in enumerate(entries):
            has_children = any(path.startswith(entry.ref_id + '/') for path in tree_map)
            if has_children:
                self.nodes[idx].is_index = True
            
        print(f"RefTree built with {len(self.nodes)} nodes")