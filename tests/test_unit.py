"""Unit Test suite for open_dm_ref_splitter"""

import re
import pytest
from src.dm_ref import DMRef

@pytest.mark.unit
def test_byond_remote_url() -> None:
    """ensures that DMRef is checking the correct url"""
    ref: DMRef = DMRef()
    assert ref.dm_ref_url == "https://www.byond.com/docs/ref/info.html"
    print("BYOND reference URL is correct")

@pytest.mark.unit
def test_timeout_safeguard() -> None:
    """Ensures that setting a timeout greater than 10 seconds raises a ValueError."""
    safe_regex: str = re.escape(DMRef.timeout_error_message)
    with pytest.raises(ValueError, match=safe_regex):
        DMRef(timeout_seconds=15)
    print("Timeout safeguard in place")