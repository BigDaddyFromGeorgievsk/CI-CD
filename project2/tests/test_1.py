#!/usr/bin/python3

import pytest

def reminder_two_numbers(a, b):
	return a % b

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (11, 3, 2),
    (12, 4, 0),
    (21, 3, 0),
    (26, 4, 2),
    ])
def test_reminder_two_numbers(a, b, expected):
  assert reminder_two_numbers(a, b) == expected
