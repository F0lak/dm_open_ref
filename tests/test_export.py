'''
Tests the markdown export script
'''
import pytest
from pathlib import Path, PurePosixPath
from unittest.mock import patch
from ref_splitter.export import ExportMD, MDFlavour, MDPage
from ref_splitter.token_table import INLINE_TOKEN_TABLE, P_CLASS_TOKEN_TABLE

@pytest.fixture(scope="module")
def export_instance():
    '''module scoped export md instance'''
    return ExportMD("_tmp_test")

MOCK_TOKEN_TABLE: list[dict] = [
        {"TOKEN" : "BOLD", "md" : "**"},
        {"TOKEN" : "CODE", "md" : "`"},
        {"TOKEN" : "ITALIC", "md" : "*"}
        # Any invalid data here will be flagged in the following test, aborting the suite.
    ]

@pytest.mark.unit
def test_mock_token_table_is_correct_subset_of_inline_token_table():
    '''Ensures mock rows exist exactly as defined in the inline table'''
    inline_lookup = {}
    for row in INLINE_TOKEN_TABLE:
        inline_lookup[row["TOKEN"]] = row["md"]
    
    for mock_row in MOCK_TOKEN_TABLE:
        for key in mock_row:
            if key not in ["TOKEN", "md"]:
                pytest.exit(f'Aborting suite: Unexpected key "{key}" in MOCK_TOKEN_TABLE row: {mock_row}', returncode=1)
        token = mock_row["TOKEN"]
        if token not in inline_lookup:
            pytest.exit(f'Aborting suite: {token} is not present in source token table', returncode=1)
        if mock_row["md"] != inline_lookup[token]:
            pytest.exit(f'Aborting suite: MOCK_TOKEN_TABLE does not match source token table. ({mock_row["md"]} != {inline_lookup[token]})', returncode=1)

@pytest.mark.unit
def test_format_string_list(export_instance) -> None:
    '''ensures format_string_list formats a string list correctly'''
    data: list[str] = [
        "test1",
        "test2"
    ]
    expected = "\n**TEST:**\n+   test1\n+   test2\n"
    assert export_instance.format_string_list(data, "TEST") == expected
    
@pytest.mark.unit
@pytest.mark.parametrize("flavour", list(MDFlavour))
def test_string_seasoning(flavour: MDFlavour, export_instance) -> None:
    data = "\ntest1\ntest2\ntest3"
    expected = f'\n> [!{flavour.value}]\n> test1\n> test2\n> test3'
    assert export_instance.season_string(data, flavour) == expected
    
@pytest.mark.unit
@pytest.mark.parametrize("row", MOCK_TOKEN_TABLE)
def test_format_tokens(row, export_instance) -> None:
    '''ensures that format_tokens() properly replaces
    tokens with their md counterparts in the MOCK_TOKEN_TABLE'''
    data: str = f'[{row["TOKEN"]}]test[/{row["TOKEN"]}]'
    expected: str = f'{row["md"]}test{row["md"]}'
    
    assert export_instance.format_tokens(data) == expected
    
@pytest.mark.unit
@pytest.mark.parametrize("row", MOCK_TOKEN_TABLE)
def test_format_tokens_removing_whitespace(row, export_instance) -> None:
    '''ensures that format_tokens() properly removes whitespace inside the token'''
    data: str = f'[{row["TOKEN"]}] test [/{row["TOKEN"]}]'
    expected: str = f'{row["md"]}test{row["md"]}'
    
    assert export_instance.format_tokens(data) == expected
    
@pytest.mark.integration
@pytest.mark.parametrize("row", INLINE_TOKEN_TABLE)
def test_format_inline_tokens(row, export_instance) -> None:
    '''ensures the INLINE_TOKEN_TABLE is not malformed
    and it can be reformatted correctly'''
    data: str = f'[{row["TOKEN"]}] test [/{row["TOKEN"]}]'
    expected: str = f'{row["md"]}test{row["md"]}'
    
    assert export_instance.format_tokens(data) == expected
    
@pytest.mark.unit
def test_format_codeblock(export_instance) -> None:
    '''ensures codeblocks are formatted correctly'''
    data: str = "[CODEBLOCK]proc/foo() {bar}[/CODEBLOCK]\n[CODEBLOCK]proc/foo()\n\tbar[/CODEBLOCK]"
    expected: str = "\n```dm\nproc/foo() {bar}\n```\n\n\n```dm\nproc/foo()\n\tbar\n```\n"
    
    assert export_instance.format_codeblocks(data) == expected
    
@pytest.mark.unit
def test_format_links(export_instance) -> None:
    '''ensures links are paarsed to the correct markdown format'''
    test_dict = {"/path" : "text"}
    data: str = "[LINK]/path[/LINK]"
    expected: str = " [text](/ref/path)"

    assert export_instance.format_links(test_dict, data) == expected
    
@pytest.mark.unit
def test_export_page_configurable(tmp_path) -> None:
    '''ensures exporting a page properly writes a file to disk'''
    injector = ExportMD(exp_path=tmp_path)
    
    page = MDPage("test/page", "test content", False)
    injector.export_page(page)
    
    expected_file = tmp_path / "ref" / "test" / "page.md"
    assert expected_file.exists()
    assert expected_file.read_text(encoding="utf-8") == "test content"
    
@pytest.mark.unit
def test_export_page_linux_behavior(tmp_path):
    '''Simulates Linux path behavior on Windows to catch OS issues locally'''
    injector = ExportMD(exp_path=tmp_path)
    page = MDPage("test/page", "test content", False)
    
    with patch('pathlib.Path', PurePosixPath):
        clean_ref_id = page.id.lstrip("\\/")
        clean_filepath = injector.clean_filepath(clean_ref_id)
        
        export_file = Path(f"{clean_filepath}.md") 
        print(f"\nLinux Path Parts: {export_file.parts}") 
        
        assert len(export_file.parts) == 2, "Linux failed to split the directory!"