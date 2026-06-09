"""
Network related tests
currently only checks if the BYOND reference can be accessed
"""

import pytest
from ref_splitter.dm_ref import DMRef

@pytest.mark.network
def test_fetch_ref_from_byond_server() -> None:
    """creates a DMRef object and attempts to download the reference from BYOND remote"""
    ref: DMRef = DMRef()
    ref.fetch_web_ref()

    assert len(ref.ref_info) > 0
    print(f"reference file is {len(ref.ref_info)} characters long")
