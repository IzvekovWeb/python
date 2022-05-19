from hexlet_pytest import __version__
from hexlet_pytest import fill
import pytest

@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


# BEGIN (write your solution here)
def test_fill_start_end_default(collection):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']
def test_fill_end_default(collection):
    fill(collection, '*', 1)
    assert collection ==  [1, '*', '*', '*']
def test_fill_in_middle(collection):
    fill(collection, '*', 1, 3)
    assert collection ==  [1, '*', '*', 4]
def test_fill_out_of_end_index(collection):
    fill(collection, '*', 0, 10)
    assert collection ==  ['*', '*', '*', '*']
# END