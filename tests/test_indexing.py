import numpy as np

def test_basic_indexing():
    arr = np.array([10, 20, 30])
    assert arr[0] == 10
    assert arr[-1] == 30


def test_slicing():
    arr = np.arange(10)
    np.testing.assert_array_equal(arr[:3], np.array([0, 1, 2]))
    np.testing.assert_array_equal(arr[-3:], np.array([7, 8, 9]))


def test_boolean_mask():
    arr = np.array([1, 2, 3, 4, 5])
    expected = np.array([4, 5])
    np.testing.assert_array_equal(arr[arr > 3], expected)


def test_fancy_indexing():
    arr = np.arange(10)
    expected = np.array([0, 2, 5])
    np.testing.assert_array_equal(arr[[0, 2, 5]], expected)