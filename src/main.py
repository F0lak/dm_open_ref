'''
Main File to extract and parse the DM reference from remote
'''

from dm_ref import DMRef
from ref_splitter import RefSplitter

ref = DMRef()
ref.fetch_web_ref()

splitter = RefSplitter(ref.ref_str)

limit: int = 5
splitter.build_ref_entries(limit)
splitter.save_pretty_soup()
print("Finished")
