'''
Main File to extract and parse the DM reference from remote
'''

from .dm_ref import DMRef
from .ref_splitter import RefSplitter
from .ref_tree import RefTree
from .export import ExportMD

ref = DMRef()
splitter = RefSplitter(ref.fetch_web_ref())
splitter.prep_pages()
splitter.build_ref_entries()

ref_tree: RefTree = RefTree()
ref_tree.links = splitter.links
ref_tree.build_tree_from_entries(splitter.entries, splitter.links)

export = ExportMD()
export.export(ref_tree)
