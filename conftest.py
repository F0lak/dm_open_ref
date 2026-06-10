from pathlib import Path
import pytest
from ref_splitter.ref_splitter import RefSplitter

@pytest.fixture(scope="function")
def mouse_down_sample_path():
    """Returns the absolute path to the mouse_down_sample test file."""
    return Path(__file__).parent / "tests" / "test_data" / "mouse_down_input_sample.txt"

@pytest.fixture(scope="function")
def client_sample_path():
    """Returns the absolute path to the reference client sample file."""
    return Path(__file__).parent / "tests" / "test_data" / "ref_client_input_sample.txt"

@pytest.fixture(scope="function")
def splitter(mouse_down_sample_path):
    '''creates a shared splitter instance for all the tests in this module'''
    with open(mouse_down_sample_path, 'r', encoding='utf-8') as f:
        content = f.read()

    splitter_instance = RefSplitter(content)
    splitter_instance.prep_pages()
    splitter_instance.build_ref_entries()

    return splitter_instance
