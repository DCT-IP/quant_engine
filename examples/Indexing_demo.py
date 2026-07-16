import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("First element:", arr[0])
print("Last element:", arr[-1])
print("Third element:", arr[2])

matrix = np.arange(1, 10).reshape(3, 3)

print("\nMatrix:")
print(matrix)

print("Element (0,1):", matrix[0, 1])
print("Element (2,2):", matrix[2, 2])