## Exercise 3 (Python) — Write the Algorithm

Given a list of non-negative integers representing histogram bar heights (each bar has width 1), compute the area of the largest rectangle that fits entirely within the histogram.

**Input:** `heights: list[int]`  
**Output:** `int`

**Constraints:** O(n) time required. Include a brief justification of your approach and its complexity.

**Tests:**
```python
assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle([2, 4]) == 4
assert largest_rectangle([1]) == 1
assert largest_rectangle([0, 0, 0]) == 0
assert largest_rectangle([6, 2, 5, 4, 5, 1, 6]) == 12
```