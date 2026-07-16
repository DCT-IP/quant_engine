import numpy as np

prices = np.array([101, 98, 105, 94, 110])

print("Prices:", prices)

print("\nMask >100:")
print(prices > 100)

print("\nPrices >100:")
print(prices[prices > 100])

print("\nEven prices:")
print(prices[prices % 2 == 0])

print("\nPrices <100:")
print(prices[prices < 100])