'''
Main File to extract and parse the DM reference from remote
'''

from src.dm_ref import DMRef
from src.ref_splitter import RefSplitter
from src.ref_tree import RefTree

ref = DMRef()
#ref.fetch_web_ref()

#sample_path = "./mouse_down_sample.txt"
#with open(sample_path, 'r', encoding='utf-8') as f:
#    sample_string = f.read()

splitter = RefSplitter(ref.fetch_web_ref())

#limit: int = 5
splitter.build_ref_entries()
#splitter.save_pretty_soup()

ref_tree: RefTree = RefTree()
ref_tree.links = splitter.links
ref_tree.build_tree_from_entries(splitter.entries)
ref_tree.export_markdown()

print("Finished")
