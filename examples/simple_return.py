import numpy as np

prices = np.array([100,105,103,110])
returns = prices[1:] / prices[:-1] - 1

print("Prices")
print(prices)

print()

print("Simple Returns")
print(returns)