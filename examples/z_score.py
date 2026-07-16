import numpy as np

data = np.array([15,18,21,30,45])

z = (data-data.mean())/data.std()

print(z)