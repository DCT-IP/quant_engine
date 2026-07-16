import numpy as np

prices = np.array([100,105,103,108,110])

normalized = (prices - prices.mean()) / prices.std()

print("Original")

print(prices)

print()

print("Normalized")

print(normalized)