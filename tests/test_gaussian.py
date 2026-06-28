
import pytest

from quant_eng.math.gaussian import solve

def test_2x2_system():
    A = [
        [2.0, 1.0],
        [1.0, 3.0]
    ]
    b = [5.0, 6.0]
    expected = [1.8, 1.4]
    assert solve(A, b) == pytest.approx(expected)


def test_3x3_system():
    A = [
        [2.0, 1.0, 1.0],
        [4.0, -6.0, 0.0],
        [-2.0, 7.0, 2.0]
    ]
    b = [5.0, -2.0, 9.0]
    expected = [1.0, 1.0, 2.0]
    assert solve(A, b) == pytest.approx(expected)


def test_identity_matrix():
    A = [
        [1.0, 0.0],
        [0.0, 1.0]
    ]
    b = [10.0, 20.0]
    assert solve(A, b) == pytest.approx([10.0, 20.0])


def test_single_equation():
    A = [[5.0]]
    b = [10.0]
    assert solve(A, b) == pytest.approx([2.0])


def test_empty_matrix():
    with pytest.raises(ValueError):
        solve([], [])


def test_non_square_matrix():
    A = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ]
    b = [1.0, 2.0]
    with pytest.raises(ValueError):
        solve(A, b)


def test_dimension_mismatch():
    A = [
        [1.0, 2.0],
        [3.0, 4.0]
    ]
    b = [1.0]
    with pytest.raises(ValueError):
        solve(A, b)


def test_non_numeric_matrix():
    A = [
        [1.0, "hello"],
        [3.0, 4.0]
    ]
    b = [1.0, 2.0]
    with pytest.raises(TypeError):
        solve(A, b)


def test_non_numeric_vector():
    A = [
        [1.0, 2.0],
        [3.0, 4.0]
    ]
    b = [1.0, "world"]
    with pytest.raises(TypeError):
        solve(A, b)


def test_requires_partial_pivoting():
    A = [
        [0.0, 2.0],
        [1.0, 3.0]
    ]
    b = [4.0, 5.0]

    expected = [-1.0, 2.0]
    assert solve(A, b) == pytest.approx(expected)


def test_singular_matrix():
    A = [
        [1.0, 2.0],
        [2.0, 4.0]
    ]
    b = [3.0, 6.0]
    with pytest.raises(ValueError):
        solve(A, b)


def test_original_matrix_unchanged():
    A = [
        [2.0, 1.0],
        [1.0, 3.0]
    ]
    original = [
        [2.0, 1.0],
        [1.0, 3.0]
    ]
    b = [5.0, 6.0]
    solve(A, b)
    assert A == original
