'''Integration test to ensure that RefSplitter can properly parse a test file'''
import pytest
from src.ref_splitter import RefSplitter

@pytest.fixture(scope="module")
def splitter():
    '''creates a shared splitter instance for all the tests in this module'''
    sample_path = './mouse_drop_sample.txt'
    with open(sample_path, 'r', encoding='utf-8') as f:
        content = f.read()

    splitter_instance = RefSplitter(content)
    splitter_instance.build_ref_entries()

    return splitter_instance

@pytest.mark.integration
def test_data_population(splitter) -> None:
    '''tests that the splitter populated its data fields'''
    assert len(splitter.entries) > 0
    assert len(splitter.pages) > 0
    assert len(splitter.links) > 0

@pytest.mark.integration
def test_description_list_parsed(splitter) -> None:
    '''ensures that the description lists were populated, and properly'''
    assert len(splitter.entries) > 0
    first_entry = splitter.entries[0]
    assert isinstance(first_entry.desc_lists, dict)
    assert len(first_entry.desc_lists) > 0
