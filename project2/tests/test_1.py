#!/usr/bin/python3

import pytest

def reminder_two_numbers(a, b):
   try:
    return a % b
  except ZeroDivisionError:
  
    return None

@pytest.mark.parametrize("a, b, expected", [
    (10, 3, 1),
    (11, 3, 2),
    (12, 4, 0),
    (-10, 3, -1),
    (-11, 3, -2),
    (10, 0, "Деление на ноль невозможно!"),
])
def test_reminder_two_numbers(a, b, expected):
  assert reminder_two_numbers(a, b) == expected
