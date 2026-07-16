# Broadcasting
## What is Broadcasting?
Broadcasting is NumPy's mechanism for performing element-wise operations on arrays of different shapes without explicitly copying data.
---
## Why is Broadcasting Useful?

- Eliminates Python loops
- Improves readability
- Faster execution
- Lower memory usage
---
## Broadcasting Rules
NumPy compares array shapes from right to left.
Two dimensions are compatible if:
- They are equal
- One of them is 1
Otherwise, a ValueError is raised.
---
## Examples
### Scalar Broadcasting
```python
arr + 5
```
### Row Broadcasting
```python
matrix + vector
```
### Column Broadcasting
```python
matrix + column_vector
```
---
## Common Errors
Attempting to combine arrays whose shapes are incompatible.
Example:
```python
(2,3) + (4,)
```
Raises a ValueError.
---
## Why is Broadcasting Fast?
Broadcasting avoids allocating additional memory by reusing existing data through NumPy's internal stride mechanism.
---