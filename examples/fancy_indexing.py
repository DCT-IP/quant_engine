import numpy as np

arr = np.arange(10)

print("Array:", arr)

print("Selected elements:")
print(arr[[0, 3, 5, 8]])

matrix = np.arange(1, 17).reshape(4, 4)

print("\nMatrix:")
print(matrix)

print("\nRows 0 and 2:")
print(matrix[[0, 2]])

print("\nColumns 1 and 3:")
print(matrix[:, [1, 3]])