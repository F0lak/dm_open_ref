'''Integration test to ensure that RefSplitter can properly parse a test file'''
import pytest
from src.ref_splitter import RefSplitter, RefEntry, TOKEN_TABLE
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

@pytest.mark.unit
@pytest.mark.dependency(name="desc_list")
def test_desc_list_parsing(splitter) -> None:
    '''confirms that desc_lists is populating correctly'''
    
    # DM Ref only ever has one term per list, so there's no need to parse more than one.
    # this would need to be changed when the standard for the html ref is modernized
    sample: str = '''
    <div>
    <dl>
        <dt>term1</dt>
            <dd>1</dd>
            <dd>2</dd>
            <dd>3</dd>
            <dd>4</dd>
            <dd>5</dd>
    </dl>
    </div>
    '''
    soup = BeautifulSoup(sample, "lxml")
    tag = soup.find('div')
    
    desc_lists = splitter.format_description_lists(tag)
    
    assert isinstance(desc_lists, dict)
    assert len(desc_lists) == 1, f'desc_lists size is incorrect.  expected 1, got {len(desc_lists)}\ndesc_lists = {desc_lists}'
    
    assert isinstance(desc_lists["term1"], list)
    assert len(desc_lists["term1"]) == 5

@pytest.mark.integration
@pytest.mark.dependency(depends=["desc_list"])
@pytest.mark.parametrize("input_field", [
    field
    for field in RefSplitter.field_mapping
])
def test_common_field_parsing(splitter, input_field) -> None:
    '''ensures that the description lists are parsed into common fields properly'''
    soup = BeautifulSoup(f'<div><dl><dt>{input_field}</dt><dd>test</dd></dl></div>', "lxml")
    tag = soup.find('div')
    
    desc_lists = splitter.format_description_lists(tag)
    entry: RefEntry = RefEntry("/test")
    splitter.set_common_fields(entry, desc_lists)
    
    attr_name = splitter.field_mapping[input_field]
    attr_value = getattr(entry, attr_name)
    
    assert isinstance(attr_value, list)
    assert len(attr_value) > 0
    

@pytest.mark.unit
@pytest.mark.parametrize(
    "html_input, expected_output",
    [
        ("<b>bold</b>", "[BOLD]bold[/BOLD]"),
        ("<i>italic</i>", "[ITALIC]italic[/ITALIC]"),
        ("<u>underline</u>", "[UNDERLINE]underline[/UNDERLINE]"),
        ("<tt>typetext</tt>", "[CODE]typetext[/CODE]"),
        ("<var>var</var>", "[CODE]var[/CODE]"),
        ("<dt>term</dt>", "[DESC_TERM]term[/DESC_TERM]"),
        ("<dd>detail</dd>", "[DESC_DETAIL]detail[/DESC_DETAIL]")
    ],
)
def test_inline_tag_tokenization(splitter, html_input, expected_output) -> None:
    '''ensures that inline tokens are generated correctly'''
    assert splitter.tokenize(html_input) == expected_output
    
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
    '''
    ensures page parsing will throw an exception when
    it encounters a non-existant or malformed tag
    '''
    
    with pytest.raises(ValueError):
        splitter.clean_paragraph(bad_input)

@pytest.mark.unit
def test_token_table_values() -> None:
    '''
    Ensures structural values inside the token table are
    clean, not empty, and don't have formatting artifacts
    '''
    for row in TOKEN_TABLE:
        html = row["html"]
        token = row["TOKEN"]
        
        assert html.strip(), "Found an empty 'html' tag configuration"
        assert token.strip(), f"Found an empty token configuration for tag '{html}'"
        
        assert "<" not in html and ">" not in html, f"Remove bracket symbols from html configuration key: '{html}'"
        assert "[" not in token and "]" not in token, f"Remove bracket symbols from TOKEN configuration value: '{token}'"