import numpy as np

from quant_eng.statistics.rolling import (
    rolling_mean,
    rolling_std,
    rolling_min,
    rolling_max,
)


prices = np.array([
    100,
    102,
    101,
    105,
    107,
    106,
    110,
])

window = 3


print("Prices:")
print(prices)

print("\nRolling Mean:")
print(rolling_mean(prices, window))

print("\nRolling Standard Deviation:")
print(rolling_std(prices, window))

print("\nRolling Minimum:")
print(rolling_min(prices, window))

print("\nRolling Maximum:")
print(rolling_max(prices, window))