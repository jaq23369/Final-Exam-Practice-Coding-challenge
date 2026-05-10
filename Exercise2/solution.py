# Exercise 2 — Improve This Algorithm
# Compute the n-th Fibonacci number.

# === Original implementation analysis ===
# Time:  O(2^n) — each call branches into 2, forming a binary tree of depth n
# Space: O(n)   — recursive call stack grows up to n frames deep

# === Optimized implementation (bottom-up DP) ===
# Instead of going top-down and recalculating, start from fib(0) and fib(1)
# and build upward. Only keep the last two values (sliding window of size 2).


def fib(n: int) -> int:
    if n <= 1:                         # base cases: fib(0)=0, fib(1)=1
        return n

    prev, curr = 0, 1                  # start with fib(0) and fib(1)

    for _ in range(2, n + 1):          # compute fib(2), fib(3), ..., fib(n)
        prev, curr = curr, prev + curr # slide the window forward

    return curr                        # curr now holds fib(n)

# Time:  O(n) — single loop from 2 to n
# Space: O(1) — only two variables, no recursion, no array


# ---------- Tests ----------
if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55
    assert fib(30) == 832040

    print("All tests passed!")
