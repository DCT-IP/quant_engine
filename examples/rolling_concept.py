import numpy as np

from numpy.lib.stride_tricks import sliding_window_view


data = np.array([10, 20, 30, 40, 50])

windows = sliding_window_view(data, 3)

print("Data:")
print(data)

print("\nWindows:")
print(windows)

print("\nMean of each window:")
print(np.mean(windows, axis=1))