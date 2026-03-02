from src.tasks.task0.main import count_words


def test_count_words():
    assert count_words('test string for script test') == {
        'test': 2,
        'string': 1,
        'for': 1,
        'script': 1
    }
