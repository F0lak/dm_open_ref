'''
Series of tests ran on the ref_splitter's encode_link() function
'''

import pytest
from ref_splitter.ref_splitter import RefSplitter
from bs4 import Tag

@pytest.mark.unit
def test_encode_link() -> None:
    '''confirms that refsplitter can create correct links'''
    mock_html = '<a href="#/DM/mouse">mouse handling</a>'
    splitter = RefSplitter(mock_html)
    mock_a_tag: Tag | None = splitter.soup.find('a')

    # couple quick tests to make sure bs4 is working
    assert mock_a_tag is not None
    assert mock_a_tag.name == "a"

    splitter.encode_link(mock_a_tag)

    assert len(splitter.links) == 1
    assert '/DM/mouse' in splitter.links
    assert splitter.links['/DM/mouse'] == "mouse handling"

@pytest.mark.unit
def test_encode_link_none_input():
    '''confirms that we get an error when the tag is passed as None'''
    splitter = RefSplitter("")

    with pytest.raises(TypeError, match="a Tag is 'None'"):
        splitter.encode_link(None)

@pytest.mark.unit
def test_encode_link_invalid_tag():
    '''confirms that we raise a value error when we pass in a non <a> tag'''
    splitter = RefSplitter('<div>Not an A tag</div>')
    invalid_tag = splitter.soup.div

    with pytest.raises(RuntimeError, match="Trying to encode an invalid tag"):
        splitter.encode_link(invalid_tag)

@pytest.mark.unit
def test_encode_link_missing_href():
    '''confirms that we get an error when the href attribute is missing'''
    splitter = RefSplitter('<a>No Href</a>')
    missing_href_tag = splitter.soup.a

    # Verifies it raises ValueError when href attribute is missing
    with pytest.raises(ValueError, match="a Tag does not have href attribute"):
        splitter.encode_link(missing_href_tag)

@pytest.mark.unit
@pytest.mark.parametrize("html_input", [
    '<a href="#">Empty Path</a>',
    '<a href="">Empty Path</a>',
    '<a href=>Empty Path</a>'
])
def test_encode_link_empty_paths(html_input: str):
    '''confirms that we get a value error when the path is only a 1 character long'''
    splitter = RefSplitter(html_input)
    target_tag = splitter.soup.a

    # Verifies it raises ValueError when path is just "#" (becomes empty string)
    with pytest.raises(ValueError, match="Empty link path"):
        splitter.encode_link(target_tag)
