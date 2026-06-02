'''
RefNode and RefTree classes for organizing the parsed information into a digestible tree.
'''

from src.ref_splitter import RefEntry
import pathlib


class RefNode:
    '''A reference tree node for organizing the reference tree content'''
    id: int
    entry: RefEntry
    
    def __init__(self, entry, id: int) -> None:
        self.entry = entry
        self.id = id

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
        
    def build_tree_from_entries(self, entries: list[RefEntry]) -> None:
        for entry in entries:
            new_node = self.create_node(entry)
            self.append(new_node)
            
        print(f"RefTree built with {len(self.nodes)} nodes")
            
    def append(self, node: RefNode) -> None:
        self.nodes.append(node)
    
    def create_node(self, entry: RefEntry) -> RefNode:
        new_node = RefNode(entry, len(self.nodes))
        return new_node

    def export_markdown(self) -> None:
        for node in self.nodes:
            clean_ref_id = node.entry.ref_id.lstrip("\\/")
            
            export_file = pathlib.Path("_md_export") / clean_ref_id / f"{node.entry.title}.md"
            print(f"Writing {export_file}")
            export_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(export_file, "w", encoding="utf-8") as file:
                file.write(node.entry.content)