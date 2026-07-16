import numpy as np


a = np.array([1, 2, 3])

print("Array:", a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Size:", a.size)
print("Dtype:", a.dtype)
print("Itemsize:", a.itemsize)
print("Total Bytes:", a.nbytes)

print()

zeros = np.zeros((3, 3))
print(zeros)

print()

ones = np.ones((2, 5))
print(ones)

print()

identity = np.eye(4)
print(identity)

print()

numbers = np.arange(0, 10)
print(numbers)

print()

line = np.linspace(0, 1, 5)
print(line)