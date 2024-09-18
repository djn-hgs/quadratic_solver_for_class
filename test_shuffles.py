import math
import pytest

from shuffles_solution import count_shuffles

test_data = [
    ('GAL', math.factorial(3)),
    ('TOMAS', math.factorial(5)),
    ('HEATH', math.factorial(5) / math.factorial(2)),
    ('HEATHER', math.factorial(7) / (math.factorial(2) * math.factorial(2))),
    ('BOBBY', math.factorial(5) / math.factorial(3)),
]

@pytest.mark.parametrize('word, count', test_data)
def test_count_shuffles(word, count):
    assert count_shuffles(word) == count

