**Precondition:**

```python
1 < len(cube) <= 5
len(cube) == len(cube[0]) == len(cube[0][0])
all(all(all(ch in "XZ" for ch in row) for row in grid) for grid in cube)
```