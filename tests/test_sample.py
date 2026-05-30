'''
Unit Test suite for open_dm_ref_splitter
'''

def func(x: int) -> int:
    '''returns x + 1'''
    return x + 1

def test_answer() -> None:
    '''Runs test for the answer'''
    assert func(3) == 4

def failing_test() -> None:
    '''A deliberately failing test'''
    assert 1 == 1
    assert 1 == 2
    assert 2 == 2

def passing_test() -> None:
    '''A deliberately passing test'''
    assert 1 == 1
    assert "tits" == "tits"
