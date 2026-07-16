import numpy as np

def test_view_shares_memory():
    arr = np.arange(10)
    view = arr[2:5]
    view[0] = 100
    assert arr[2] == 100


def test_copy_does_not_share():
    arr = np.arange(10)
    copy = arr[2:5].copy()
    copy[0] = 100
    assert arr[2] != 100