import numpy as np
import pytest

from quant_eng.statistics.rolling import (
    rolling_mean,
    rolling_std,
    rolling_min,
    rolling_max,
)


def test_rolling_mean():

    data = np.array([1, 2, 3, 4, 5])

    expected = np.array([
        2.0,
        3.0,
        4.0,
    ])

    result = rolling_mean(data, 3)

    np.testing.assert_allclose(
        result,
        expected,
    )


def test_rolling_std():

    data = np.array([1, 2, 3, 4, 5])

    expected = np.array([
        np.std([1, 2, 3]),
        np.std([2, 3, 4]),
        np.std([3, 4, 5]),
    ])

    result = rolling_std(data, 3)

    np.testing.assert_allclose(
        result,
        expected,
    )


def test_rolling_min():

    data = np.array([5, 2, 8, 1, 7])

    expected = np.array([
        2,
        1,
        1,
    ])

    result = rolling_min(data, 3)

    np.testing.assert_array_equal(
        result,
        expected,
    )


def test_rolling_max():

    data = np.array([5, 2, 8, 1, 7])

    expected = np.array([
        8,
        8,
        8,
    ])

    result = rolling_max(data, 3)

    np.testing.assert_array_equal(
        result,
        expected,
    )


def test_window_must_be_positive():

    data = np.array([1, 2, 3])

    with pytest.raises(ValueError):
        rolling_mean(data, 0)


def test_window_cannot_exceed_data():

    data = np.array([1, 2, 3])

    with pytest.raises(ValueError):
        rolling_mean(data, 4)


def test_data_must_be_ndarray():

    with pytest.raises(TypeError):
        rolling_mean([1, 2, 3], 2)


def test_data_must_be_one_dimensional():

    data = np.array([
        [1, 2],
        [3, 4],
    ])

    with pytest.raises(ValueError):
        rolling_mean(data, 2)


def test_empty_data():

    data = np.array([])

    with pytest.raises(ValueError):
        rolling_mean(data, 2)


def test_window_equal_to_data_length():

    data = np.array([1, 2, 3])

    result = rolling_mean(data, 3)

    expected = np.array([2.0])

    np.testing.assert_allclose(
        result,
        expected,
    )