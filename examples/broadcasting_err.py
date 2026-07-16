import numpy as np

a = np.ones((2,3))

b = np.ones((4,))

try:
    print(a + b)
except ValueError as e:
    print(e)