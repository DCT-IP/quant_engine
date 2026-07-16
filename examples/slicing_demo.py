import numpy as np

arr = np.arange(1, 11)

print("Original:", arr)

print("First five:", arr[:5])
print("Last five:", arr[-5:])
print("Middle:", arr[2:7])
print("Every second:", arr[::2])
print("Reverse:", arr[::-1])

matrix = np.arange(1, 26).reshape(5, 5)

print("\nMatrix:")
print(matrix)

print("\nFirst row:")
print(matrix[0])

print("\nFirst column:")
print(matrix[:, 0])

print("\nCenter 3x3:")
print(matrix[1:4, 1:4])

print("\nLast column:")
print(matrix[:, -1])