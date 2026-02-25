import pytest
from src.tasks.task1.main import count_words

def test_count_words():
    assert count_words('test string for script test') == {
        'test': 2,
        'string': 1,
        'for': 1,
        'script': 1
    }
