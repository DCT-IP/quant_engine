# Vectorization
## What is Vectorization?
Vectorization is the process of performing operations on entire arrays instead of iterating element-by-element using Python loops.
---
## Why Use Vectorization?
- Faster execution
- Lower memory overhead
- Cleaner code
- Takes advantage of NumPy's optimized C implementation
---
## Financial Example
Instead of
```python
for i in range(len(prices)-1):
    ...
```
Use
```python
prices[1:] / prices[:-1] - 1
```
---
## Statistics
Useful vectorized operations include:
- Mean
- Variance
- Standard Deviation
- Logarithm
- Difference
- Normalization
---