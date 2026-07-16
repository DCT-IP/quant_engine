import numpy as np

matrix = np.arange(9).reshape(3, 3)
ravel = matrix.ravel()
flatten = matrix.flatten()
ravel[0] = 100

print(matrix)
print(flatten)