'''Unit Test suite for open_dm_ref_splitter'''

import re
import pytest
from src.dm_ref import DMRef

@pytest.mark.unit
def test_byond_remote_url() -> None:
    '''ensures that DMRef is checking the correct url'''
    ref: DMRef = DMRef()
    assert ref.dm_ref_url == "https://www.byond.com/docs/ref/info.html"
    print("BYOND reference URL is correct")

@pytest.mark.unit
@pytest.mark.parametrize("timeout", [10.1, 11, 15])
def test_timeout_safeguard_failing_bounds(timeout: int) -> None:
    '''Ensures values strictly greater than 10 seconds raise a ValueError.'''
    safe_regex: str = re.escape(DMRef.timeout_error_message)
    with pytest.raises(ValueError, match=safe_regex):
        DMRef(timeout_seconds=timeout)

@pytest.mark.unit
@pytest.mark.parametrize("timeout", [0, 5, 10])
def test_timeout_safeguard_passing_bounds(timeout: int) -> None:
    '''Ensures values less than or equal to 10 seconds pass successfully.'''
    ref = DMRef(timeout_seconds=timeout)
    assert ref.timeout_seconds == timeout
