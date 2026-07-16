# Views vs Copies
## What is a View?
A view is another array object that references the same underlying memory as the original array.
Changes made through the view are reflected in the original array.
Example:
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
view = arr[1:3]
view[0] = 100
print(arr)
# [  1 100   3   4]
```
---
## What is a Copy?
A copy creates a completely new block of memory.
Changes made to the copy do not affect the original array.
Example:
```python
copy = arr[1:3].copy()
copy[0] = 500
print(arr)
# Original array remains unchanged
```
---
## Checking Memory Sharing
NumPy provides the `base` attribute.
If an array shares memory with another array, `base` points to the original array.
Example:
```python
view.base is arr
# True
copy.base is arr
# False
```
---
## reshape()
`reshape()` changes the dimensions of an array without changing its data.
Whenever possible, NumPy returns a view instead of creating a new copy.
Example:
```python
arr = np.arange(12)
matrix = arr.reshape(3, 4)
```
---
## flatten()
`flatten()` always returns a copy.
Any modifications to the flattened array do not affect the original array.
Example:
```python
flat = matrix.flatten()
```
---
## ravel()
`ravel()` returns a flattened view whenever possible.
If a view cannot be created, NumPy returns a copy.
Example:
```python
flat = matrix.ravel()
```
---
## Why Views Matter
Views avoid allocating additional memory.
Benefits:
- Faster execution
- Lower memory usage
- Better performance on large datasets
However, modifying a view also modifies the original array.
---
## When Should I Use a Copy?
Use `.copy()` when:
- The original data must remain unchanged.
- Multiple functions operate independently on the same dataset.
- Accidental modification could introduce bugs.
---
## Key Takeaways
- Slicing usually returns a view.
- `.copy()` always creates new memory.
- `reshape()` often returns a view.
- `flatten()` always copies.
- `ravel()` prefers a view.
- Views improve performance but require careful handling.
---
## Where This Will Be Used Later
This concept is important for:
- Rolling Window calculations
- Time Series analysis
- Technical Indicators
- Portfolio Analytics
- Backtesting Engine
- Market Data processing
- Risk Engine
Avoiding unnecessary copies is essential when working with millions of market data points.