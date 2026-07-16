import numpy as np

prices = np.array([100,105,103,110])

returns = np.log(prices[1:] / prices[:-1])

print("Log Returns")

print(returns)