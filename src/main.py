'''
Main File to extract and parse the DM reference from remote
'''

from src.dm_ref import DMRef
from src.ref_splitter import RefSplitter
from src.ref_tree import RefTree
from src.export import ExportMD

def run_main():
    ref = DMRef()
    splitter = RefSplitter(ref.fetch_web_ref())
    splitter.build_ref_entries()

    ref_tree: RefTree = RefTree()
    ref_tree.links = splitter.links
    ref_tree.build_tree_from_entries(splitter.entries, splitter.links)
    
    export = ExportMD()
    export.export(ref_tree)

def run_sample():
    sample_path = "./mouse_down_sample.txt"
    with open(sample_path, 'r', encoding='utf-8') as f:
       sample_string = f.read()

    splitter = RefSplitter(sample_string)

    splitter.build_ref_entries()

    ref_tree: RefTree = RefTree()
    ref_tree.links = splitter.links
    ref_tree.build_tree_from_entries(splitter.entries, splitter.links)
    
    export = ExportMD()
    export.export(ref_tree)
    
run_sample()
