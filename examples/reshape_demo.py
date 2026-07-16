import numpy as np

arr = np.arange(12)
matrix = arr.reshape(3, 4)

print(matrix)
print("Shares memory:", matrix.base is arr)