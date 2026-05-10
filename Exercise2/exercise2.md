## Exercise 2 (Python) — Improve This Algorithm

The function below computes the n-th Fibonacci number.

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Tasks:**
1. Analyze the time and space complexity of the implementation above.
2. Rewrite it using dynamic programming (bottom-up) to achieve O(n) time and O(1) space.
3. Analyze the complexity of your new version.

**Tests:**
```python
assert fib(0) == 0
assert fib(1) == 1
assert fib(10) == 55
assert fib(30) == 832040
```