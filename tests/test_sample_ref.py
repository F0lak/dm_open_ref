'''Integration test to ensure that RefSplitter can properly parse a test file'''
import pytest
from src.ref_splitter import RefSplitter
from bs4 import BeautifulSoup

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

@pytest.mark.unit
def test_inline_tag_tokenization(splitter) -> None:
    '''ensures that inline tokens are generated correctly'''
    sample_text: str = '''
    <b>bold</b>
    <i>italic</i>
    <u>underline</u>
    <tt>typetext</tt>
    <var>var</var>
    '''
    expected: str = '''
    [BOLD]bold[/BOLD]
    [ITALIC]italic[/ITALIC]
    [UNDERLINE]underline[/UNDERLINE]
    [CODE]typetext[/CODE]
    [CODE]var[/CODE]
    '''
    
    tokenized = splitter.tokenize(sample_text)
    assert tokenized == expected
    
@pytest.mark.integration
def test_page_parsing(splitter) -> None:
    '''ensures that a page parses correctly, including tokenization and code formatting'''
    sample_text = '''
    <div>
    <p>
        This is <b>bold</b> and <tt>code</tt>.
    </p>
    <xmp>
    proc/foo()
        return bar()
    </xmp>
    <p>
        Another paragraph element here.
    </p>
    </div>
    '''
    expected = [
    "This is [BOLD]bold[/BOLD] and [CODE]code[/CODE].",
    "[CODEBLOCK]\n    proc/foo()\n        return bar()\n    [/CODEBLOCK]",
    "Another paragraph element here."
    ]
    soup = BeautifulSoup(sample_text, "lxml")
    tag = soup.find('div')
    
    result = splitter.extract_content(tag)
    
    assert result == expected

@pytest.mark.unit 
@pytest.mark.parametrize("bad_input", [
    '<p>no close',
    'no open</p>',
    'p>malformed</p'
])    
def test_ptag_failure(bad_input, splitter) -> None:
    '''ensures page parsing will throw an exception when
    it encounters a non-existant or malformed tag'''
    
    with pytest.raises(ValueError):
        splitter.clean_paragraph(bad_input)