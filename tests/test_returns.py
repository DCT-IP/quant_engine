import numpy as np
import pytest

from quant_eng.finance.returns import (
    simple_return,
    log_return,
)

def test_simple_return():
    prices = np.array([100, 110])
    expected = np.array([0.10])
    np.testing.assert_allclose(
        simple_return(prices),
        expected,
    )

def test_log_return():
    prices = np.array([100, 110])
    expected = np.log(np.array([1.10]))
    np.testing.assert_allclose(
        log_return(prices),
        expected,
    )

def test_zero_price():
    prices = np.array([100, 0])
    with pytest.raises(ValueError):
        log_return(prices)

def test_single_price():
    prices = np.array([100])
    with pytest.raises(ValueError):
        simple_return(prices)