import pytest
from src.tasks.task1.main import diff_lists


@pytest.mark.parametrize('a, b, expect', [
    ([1, 12, 10, 2], [1, 15, 10, 20], [15,20]),
    ([1, 2, 3, 4], [4, 2, 6, 0], [0, 6])
])
def test_diff(a, b, expect):
    assert(
        sorted(diff_lists(
            a, 
            b
        ))) == expect