'''
Main File to extract and parse the DM reference from remote
'''

#from dm_ref import DMRef
from src.ref_splitter import RefSplitter

#ref = DMRef()
#ref.fetch_web_ref()

sample_path = "./mouse_drop_sample.txt"
with open(sample_path, 'r', encoding='utf-8') as f:
    sample_string = f.read()

splitter = RefSplitter(sample_string)

#limit: int = 5
splitter.build_ref_entries()
#splitter.save_pretty_soup()
print("Finished")
