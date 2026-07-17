import numpy as np
import pytest

from quant_eng.statistics.descriptive import (
    mean,
    variance,
    standard_deviation,
    z_score,
    normalize,
)


def test_mean():
    data = np.array([1, 2, 3, 4, 5])
    assert mean(data) == 3


def test_variance():
    data = np.array([1, 2, 3, 4, 5])
    assert np.isclose(variance(data), 2.5)


def test_standard_deviation():
    data = np.array([1, 2, 3, 4, 5])
    assert np.isclose(standard_deviation(data), np.sqrt(2.5))


def test_z_score():
    data = np.array([1, 2, 3, 4, 5])
    result = z_score(data)

    assert np.isclose(result.mean(), 0)
    assert np.isclose(result.std(), 1)


def test_normalize():
    data = np.array([5, 10, 15])

    result = normalize(data)

    assert result.min() == 0
    assert result.max() == 1


def test_empty_array():
    with pytest.raises(ValueError):
        mean(np.array([]))


def test_wrong_type():
    with pytest.raises(TypeError):
        mean([1, 2, 3])