import numpy as np


def simple_return(prices: np.ndarray) -> np.ndarray:
    """
    Compute simple returns.

    Formula:
        (P_t - P_{t-1}) / P_{t-1}
    """
    if not isinstance(prices, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if prices.size < 2:
        raise ValueError("At least two prices are required.")

    if np.any(prices[:-1] == 0):
        raise ValueError("Previous price cannot be zero.")

    return (prices[1:] - prices[:-1]) / prices[:-1]


def log_return(prices: np.ndarray) -> np.ndarray:
    """
    Compute logarithmic returns.

    Formula:
        ln(P_t / P_{t-1})
    """
    if not isinstance(prices, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if prices.size < 2:
        raise ValueError("At least two prices are required.")

    if np.any(prices <= 0):
        raise ValueError("Prices must be positive.")

    return np.log(prices[1:] / prices[:-1])