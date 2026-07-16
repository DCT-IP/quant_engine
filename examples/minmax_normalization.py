import numpy as np

data = np.array([5,10,15,20])

normalized = (data-data.min())/(data.max()-data.min())

print(normalized)