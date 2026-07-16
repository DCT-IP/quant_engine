import numpy as np

def test_scalar_broadcast():
    arr = np.array([1,2,3])
    expected = np.array([6,7,8])
    np.testing.assert_array_equal(
        arr + 5,
        expected
    )

def test_vector_broadcast():
    matrix = np.ones((2,3))
    vector = np.array([1,2,3])
    expected = np.array([
        [2,3,4],
        [2,3,4]
    ])
    np.testing.assert_array_equal(
        matrix + vector,
        expected
    )

def test_column_broadcast():
    matrix = np.ones((3,3))
    column = np.array([
        [1],
        [2],
        [3]
    ])
    expected = np.array([
        [2,2,2],
        [3,3,3],
        [4,4,4]
    ])
    np.testing.assert_array_equal(
        matrix + column,
        expected
    )

def test_normalization():
    data = np.array([1,2,3,4,5])
    normalized = (data-data.mean())/data.std()
    assert np.isclose(normalized.mean(),0)
    assert np.isclose(normalized.std(),1)