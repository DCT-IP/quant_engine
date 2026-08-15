import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

"""
We will be performing the statistical operation of rolling mean, variance and std deviation.
"""
def _validate_input(data: np.ndarray, window: int) -> None:
    if not isinstance(data, np.ndarray):
        raise TypeError("data must be a NumPy ndarray.")

    if data.ndim != 1:
        raise ValueError("data must be a one-dimensional array.")

    if len(data) == 0:
        raise ValueError("data cannot be empty.")

    if not isinstance(window, (int, np.integer)):
        raise TypeError("window must be an integer.")

    if window <= 0:
        raise ValueError("window must be greater than zero.")

    if window > len(data):
        raise ValueError(
            "window cannot be larger than the data length."
        )

def _create_window(data: np.ndarray, window: int) -> np.ndarray:
    _validate_input(data, window)
    return sliding_window_view(data, window_shape=window)

def rolling_mean(data: np.ndarray, window: int) -> np.ndarray:
    windows = _create_window(data, window)
    return np.mean(windows,axis=1)

def rolling_variance(data:np.ndarray, window:int)->np.ndarray:
    windows = _create_window(data, window)
    return np.var(windows, axis=1)

def rolling_std(
    data: np.ndarray,window: int,) -> np.ndarray:
    windows = _create_window(data, window)
    return np.std(windows, axis=1)


def rolling_min(
    data: np.ndarray,window: int,) -> np.ndarray:
    windows = _create_window(data, window)
    return np.min(windows, axis=1)


def rolling_max(data: np.ndarray,window: int,) -> np.ndarray:

    windows = _create_window(data, window)
    return np.max(windows, axis=1)