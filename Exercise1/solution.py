# Exercise 1 — Improve This Algorithm
# Find all pairs in a list that sum to a target value.

# === Original implementation analysis ===
# Time:  O(n^2) — two nested loops, n(n-1)/2 comparisons
# Space: O(1) auxiliary — only loop variables (i, j)

# === Optimized implementation ===
# Strategy: for each number, check if its complement (target - num)
# was already seen using a hash set → O(1) lookup instead of O(n) scan


def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    seen = set()       # tracks numbers already visited — O(1) lookup
    result = []

    for num in nums:
        complement = target - num          # what do I need to reach target?
        if complement in seen:             # O(1) hash set lookup
            result.append((complement, num))
        seen.add(num)                      # mark current number as seen

    return result

# Time:  O(n) — single pass, each set op is O(1) amortized
# Space: O(n) — the 'seen' set stores up to n elements


# ---------- Tests ----------
if __name__ == "__main__":
    assert sorted(find_pairs([2, 7, 4, 1, 3], 5)) == sorted([(2, 3), (4, 1)])
    assert find_pairs([1, 2, 3], 10) == []
    assert sorted(find_pairs([5, 5, 3, 7], 10)) == sorted([(5, 5), (3, 7)])

    print("All tests passed!")
