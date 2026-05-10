# Exercise 3 — Largest Rectangle in Histogram
# Given bar heights (width 1 each), find the largest rectangle area.

# === Approach: Monotonic Stack ===
# Keep a stack of indices with strictly increasing heights.
# When a shorter bar appears, pop taller bars and compute their max rectangle.
# Each bar is pushed and popped at most once → O(n) total.


def largest_rectangle(heights: list[int]) -> int:
    stack = []                             # stores indices of bars in increasing height order
    max_area = 0
    n = len(heights)

    for i in range(n):
        # pop bars that are taller than the current one
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]       # height of the bar we're evaluating
            w = i if not stack else i - stack[-1] - 1  # width between left and right boundaries
            max_area = max(max_area, h * w)

        stack.append(i)                    # push current index

    # drain remaining bars (they never found a shorter bar to the right)
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1  # right boundary is the end of the array
        max_area = max(max_area, h * w)

    return max_area

# Time:  O(n) — each index is pushed and popped at most once (amortized)
# Space: O(n) — stack holds up to n indices in the worst case


# ---------- Tests ----------
if __name__ == "__main__":
    assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle([2, 4]) == 4
    assert largest_rectangle([1]) == 1
    assert largest_rectangle([0, 0, 0]) == 0
    assert largest_rectangle([6, 2, 5, 4, 5, 1, 6]) == 12

    print("All tests passed!")
