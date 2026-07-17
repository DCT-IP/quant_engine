import numpy as np


def mean(data: np.ndarray) -> float:
    """
    Compute the arithmetic mean.

    Parameters
    ----------
    data : np.ndarray
        Input array.

    Returns
    -------
    float
        Mean of the array.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if data.size == 0:
        raise ValueError("Input array cannot be empty.")

    return np.mean(data)


def variance(data: np.ndarray, ddof: int = 1) -> float:
    """
    Compute the variance.

    Parameters
    ----------
    data : np.ndarray
    ddof : int
        Delta Degrees of Freedom.
        ddof=1 -> Sample Variance
        ddof=0 -> Population Variance
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if data.size <= ddof:
        raise ValueError("Input array is too small.")

    return np.var(data, ddof=ddof)


def standard_deviation(data: np.ndarray, ddof: int = 1) -> float:
    """
    Compute the standard deviation.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if data.size <= ddof:
        raise ValueError("Input array is too small.")

    return np.std(data, ddof=ddof)


def z_score(data: np.ndarray) -> np.ndarray:
    """
    Standardize data using Z-score normalization.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if data.size == 0:
        raise ValueError("Input array cannot be empty.")

    std = np.std(data)

    if np.isclose(std, 0):
        raise ValueError("Standard deviation is zero.")

    return (data - np.mean(data)) / std


def normalize(data: np.ndarray) -> np.ndarray:
    """
    Perform Min-Max normalization.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Input must be a NumPy array.")

    if data.size == 0:
        raise ValueError("Input array cannot be empty.")

    minimum = np.min(data)
    maximum = np.max(data)

    if np.isclose(minimum, maximum):
        raise ValueError("All values are identical.")

    return (data - minimum) / (maximum - minimum)