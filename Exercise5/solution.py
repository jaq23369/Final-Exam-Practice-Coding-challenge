# Exercise 5 — Data Structure Selection
# Real-time leaderboard with frequent score updates and instant top-10 reads.

# === Chosen data structures ===
# 1. Hash map: player_id -> current score
#    This lets us find the old score for a player in O(1) average time.
#
# 2. Ordered set keyed by (score, player_id)
#    In production this could be a balanced BST, skip list, or Redis Sorted Set.
#    It keeps players sorted so the top 10 can be read from the high end.
#
# The implementation below uses a randomized treap as the ordered set.

from __future__ import annotations

from dataclasses import dataclass
from hashlib import blake2b
from typing import Optional


Key = tuple[int, str]


@dataclass
class Node:
    key: Key
    priority: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


def priority_for(key: Key) -> int:
    raw = f"{key[0]}:{key[1]}".encode()
    return int.from_bytes(blake2b(raw, digest_size=8).digest(), "big")


def rotate_right(root: Node) -> Node:
    new_root = root.left
    assert new_root is not None
    root.left = new_root.right
    new_root.right = root
    return new_root


def rotate_left(root: Node) -> Node:
    new_root = root.right
    assert new_root is not None
    root.right = new_root.left
    new_root.left = root
    return new_root


def insert(root: Optional[Node], key: Key) -> Node:
    if root is None:
        return Node(key=key, priority=priority_for(key))

    if key < root.key:
        root.left = insert(root.left, key)
        if root.left.priority < root.priority:
            root = rotate_right(root)
    elif key > root.key:
        root.right = insert(root.right, key)
        if root.right.priority < root.priority:
            root = rotate_left(root)

    return root


def delete(root: Optional[Node], key: Key) -> Optional[Node]:
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        if root.left.priority < root.right.priority:
            root = rotate_right(root)
            root.right = delete(root.right, key)
        else:
            root = rotate_left(root)
            root.left = delete(root.left, key)

    return root


def collect_descending(root: Optional[Node], limit: int, result: list[Key]) -> None:
    if root is None or len(result) == limit:
        return

    collect_descending(root.right, limit, result)
    if len(result) < limit:
        result.append(root.key)
    collect_descending(root.left, limit, result)


class LiveLeaderboard:
    def __init__(self) -> None:
        self.scores: dict[str, int] = {}
        self.ranking: Optional[Node] = None

    def update_score(self, player_id: str, score: int) -> None:
        if player_id in self.scores:
            old_key = (self.scores[player_id], player_id)
            self.ranking = delete(self.ranking, old_key)

        self.scores[player_id] = score
        self.ranking = insert(self.ranking, (score, player_id))

    def top(self, limit: int = 10) -> list[tuple[str, int]]:
        keys: list[Key] = []
        collect_descending(self.ranking, limit, keys)
        return [(player_id, score) for score, player_id in keys]


# Score update: O(log n) expected time.
# Top-10 query: O(log n + k) expected time, where k = 10.
# Tradeoff: two structures must stay synchronized, so updates should be
# wrapped in one operation or transaction in a real distributed system.


# ---------- Tests ----------
if __name__ == "__main__":
    board = LiveLeaderboard()

    board.update_score("ana", 50)
    board.update_score("luis", 80)
    board.update_score("maria", 70)
    board.update_score("zoe", 80)

    assert board.top(3) == [("zoe", 80), ("luis", 80), ("maria", 70)]

    board.update_score("ana", 90)
    assert board.top(2) == [("ana", 90), ("zoe", 80)]

    board.update_score("luis", 40)
    assert board.top(4) == [
        ("ana", 90),
        ("zoe", 80),
        ("maria", 70),
        ("luis", 40),
    ]

    print("All tests passed!")

