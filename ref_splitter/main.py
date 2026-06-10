'''
Main File to extract and parse the DM reference from remote
'''

from .dm_ref import DMRef
from .ref_splitter import RefSplitter
from .ref_tree import RefTree
from .export import ExportMD

import logging
import warnings
from tqdm import tqdm

class TqdmLoggingHandler(logging.Handler):
    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.write(msg)  # Safely prints above any active progress bar
            self.flush()
        except Exception:
            self.handleError(record)

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)
root_logger.addHandler(TqdmLoggingHandler())

logging.captureWarnings(True)
logging.getLogger("py.warnings").setLevel(logging.CRITICAL) 
logging.getLogger("py.warnings").addHandler(TqdmLoggingHandler())


print("Fetching remote reference material...")
ref = DMRef()
raw_content = ref.fetch_web_ref()

print("Splitting and parsing reference entries...")
splitter = RefSplitter(raw_content)
splitter.prep_pages()
splitter.build_ref_entries()

print("Building hierarchical reference tree...")
ref_tree: RefTree = RefTree()
ref_tree.build_tree_from_entries(splitter.entries, splitter.links)

print("Formatting tree structure for Markdown conversion...")
export = ExportMD("_tmp_md_export")
export.format_tree(ref_tree)

assert len(export.prepared_pages) > 0, "Export did not prepare any pages"

print("Exporting Pages to temporary directory...")
export.export_pages()

print("Safely overwriting production 'ref' folder...")
export.move_to_main_folder()

print("Cleaning up temporary export directory...")
export.clear_export_dir()

print("Pipeline executed successfully! Ready to push to GitHub.")