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
logging.getLogger("py.warnings").addHandler(TqdmLoggingHandler())

ref = DMRef()
splitter = RefSplitter(ref.fetch_web_ref())
splitter.prep_pages()
splitter.build_ref_entries()

ref_tree: RefTree = RefTree()
ref_tree.build_tree_from_entries(splitter.entries, splitter.links)

export = ExportMD()
export.export(ref_tree)
