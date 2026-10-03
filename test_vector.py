import math
import pytest
from vector import Vector


def test_add():
    assert Vector([1, 2]) + Vector([3, 4]) == Vector([4, 6])

def test_scalar_both_sides():
    assert Vector([1, 2]) * 3 == 3 * Vector([1, 2]) == Vector([3, 6])

def test_dot():
    assert Vector([1, 2, 3]).dot(Vector([4, 5, 6])) == pytest.approx(32)

def test_magnitude_3_4_5():
    assert Vector([3, 4]).magnitude() == pytest.approx(5)

def test_orthogonal_dot_is_zero():
    assert Vector([1, 0]).dot(Vector([0, 1])) == pytest.approx(0)

def test_dimension_mismatch_raises():
    with pytest.raises(ValueError):
        Vector([1, 2]) + Vector([1, 2, 3])

def test_empty_raises():
    with pytest.raises(ValueError):
        Vector([])

def test_dot_commutative():
    a, b = Vector([1, -2, 3]), Vector([4, 0, -1])
    assert a.dot(b) == pytest.approx(b.dot(a))