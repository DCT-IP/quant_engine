import numpy as np

arr = np.arange(10)

view = arr[2:7]
copy = arr[2:7].copy()

view[0] = 999

print("Original:", arr)
print("View:", view)
print("Copy:", copy)

print("\nDoes view share memory?", view.base is arr)
print("Does copy share memory?", copy.base is arr)