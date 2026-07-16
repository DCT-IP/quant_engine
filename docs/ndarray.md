# NumPy Arrays
## What is an ndarray?
A NumPy ndarray is a homogeneous, N-dimensional array that stores elements
of the same data type in contiguous memory.
Unlike Python lists, NumPy arrays store raw values directly rather than
references to Python objects.
---
## Why use ndarrays?
- Faster numerical computation
- Better CPU cache utilization
- Lower memory usage
- Enables vectorized operations
---
## Important Properties
### shape
Represents the dimensions of the array.
```python
arr.shape
```
Example
```
(3,)
(3, 4)
```
---
### ndim
Number of dimensions.
```python
arr.ndim
```
---
### size
Total number of elements.
```python
arr.size
```
---
### dtype
Data type of each element.
```python
arr.dtype
```
Common types
- int32
- int64
- float32
- float64
- bool
---
### itemsize
Memory occupied by one element.
```python
arr.itemsize
```
---
### nbytes
Total memory occupied.

```python
arr.nbytes
```
---
## Common Creation Functions
- np.array()
- np.zeros()
- np.ones()
- np.arange()
- np.linspace()
- np.eye()
- np.full()
---
## Key Takeaways
- Arrays are homogeneous.
- Arrays are stored contiguously.
- dtype affects memory usage and performance.
- shape determines dimensions.
- Vectorization depends on ndarrays.
---
