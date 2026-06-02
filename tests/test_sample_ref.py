import pytest
from src.ref_splitter import RefSplitter
from bs4 import BeautifulSoup, Tag

@pytest.mark.integration
def test_parse_sample_page() -> None:
    '''runs a full page build using a sample file'''
    sample_path = './mouse_drop_sample.txt'
    with open(sample_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    splitter = RefSplitter(content)
    splitter.build_ref_entries()
    