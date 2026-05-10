## Exercise 1 (Python) — Improve This Algorithm

The function below finds all pairs in a list that sum to a target value.

```python
def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result
```

**Tasks:**
1. Analyze the time and space complexity of the implementation above.
2. Rewrite it to achieve O(n) time complexity.
3. Analyze the complexity of your new version.

**Tests:**
```python
assert sorted(find_pairs([2, 7, 4, 1, 3], 5)) == sorted([(2, 3), (4, 1)])
assert find_pairs([1, 2, 3], 10) == []
assert sorted(find_pairs([5, 5, 3, 7], 10)) == sorted([(5, 5), (3, 7)])
```