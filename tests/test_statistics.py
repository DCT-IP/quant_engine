import numpy as np

from quant_eng.statistics.descriptive import (
    z_score,
    normalize
)


def test_z_score():
    data = np.array([1,2,3,4,5])
    result = z_score(data)
    assert np.isclose(result.mean(),0)
    assert np.isclose(result.std(),1)


def test_normalize():
    data = np.array([5,10,15])
    result = normalize(data)
    assert result.min()==0
    assert result.max()==1