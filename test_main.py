"""
Test goes here

"""

from mylib.calculator import add, subtract, multiply, divide


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(7, 3) == 4


def test_multiply():
    assert multiply(2, 3) == 6


def test_division():
    assert divide(6, 3) == 2
