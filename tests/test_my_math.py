import pytest

from src.my_math import sum, multiply, difference, absolute_sum, calculate_birth_year

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply
def test_multiply():
    res = multiply(2,2)
    assert res == 4

# Check for understanding
## Test difference
def test_difference():
    res = difference(3,2)
    assert res == 1

# Work together
## Test absolute sum
def test_absolute_sum():
    res = absolute_sum(2,3)
    assert res == 5

def test_absolute_sum_2():
    res = absolute_sum(-2,-3)
    assert res == 5
# Check for understanding
## Test calculate age

def test_calculate_birthyear():
    res = calculate_birth_year(2025, 19, False)
    assert res == 2005

def test_calculate_birthyear_2():
    res = calculate_birth_year(2025, 19, True)
    assert res == 2006
