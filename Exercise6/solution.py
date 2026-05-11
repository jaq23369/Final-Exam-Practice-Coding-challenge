# Exercise 6 — Algorithm Selection
# Fastest route in a city road network with dynamic travel times.

# === Chosen strategy: A* search ===
# Use A* with current travel time as the edge weight and a geographic
# lower-bound heuristic. This fits a road network because the heuristic guides
# the search toward the destination instead of exploring as broadly as plain
# Dijkstra.

from __future__ import annotations

from dataclasses import dataclass, field
from heapq import heappop, heappush
from math import hypot


@dataclass
class RoadNetwork:
    coordinates: dict[str, tuple[float, float]]
    graph: dict[str, dict[str, float]] = field(default_factory=dict)
    max_speed: float = 1.0

    def add_road(self, start: str, end: str, travel_time: float) -> None:
        self.graph.setdefault(start, {})[end] = travel_time
        self.graph.setdefault(end, {})

    def update_travel_time(self, start: str, end: str, travel_time: float) -> None:
        if start not in self.graph or end not in self.graph[start]:
            raise ValueError("road segment does not exist")
        self.graph[start][end] = travel_time

    def heuristic(self, node: str, goal: str) -> float:
        x1, y1 = self.coordinates[node]
        x2, y2 = self.coordinates[goal]
        return hypot(x2 - x1, y2 - y1) / self.max_speed

    def fastest_route(self, start: str, goal: str) -> tuple[float, list[str]]:
        frontier: list[tuple[float, str]] = []
        heappush(frontier, (0, start))

        came_from: dict[str, str | None] = {start: None}
        best_time: dict[str, float] = {start: 0}

        while frontier:
            _, current = heappop(frontier)

            if current == goal:
                return best_time[current], reconstruct_path(came_from, goal)

            for neighbor, travel_time in self.graph[current].items():
                new_time = best_time[current] + travel_time

                if neighbor not in best_time or new_time < best_time[neighbor]:
                    best_time[neighbor] = new_time
                    priority = new_time + self.heuristic(neighbor, goal)
                    came_from[neighbor] = current
                    heappush(frontier, (priority, neighbor))

        raise ValueError("no route found")


def reconstruct_path(came_from: dict[str, str | None], goal: str) -> list[str]:
    path = []
    current: str | None = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    return path[::-1]


# Dynamic weights:
# The road topology stays stable, while each edge's travel_time can be updated
# as traffic, rush hour, or incidents change. Each route request runs A* using
# the latest edge weights. At production scale, add short-lived caching and
# regional invalidation for affected roads.
#
# Alternative considered:
# Dijkstra is correct for non-negative travel times, but it explores more of
# the graph because it has no destination heuristic. Floyd-Warshall is ruled
# out because O(V^3) is unrealistic for about 50,000 intersections and dynamic
# edge weights would make precomputed paths stale.
#
# Time:  O((V + E) log V) worst case with a binary heap, often less in practice
#        because A* is guided by the heuristic.
# Space: O(V) for distances, parent links, and the priority queue.


# ---------- Tests ----------
if __name__ == "__main__":
    network = RoadNetwork(
        coordinates={
            "A": (0, 0),
            "B": (1, 0),
            "C": (2, 0),
            "D": (1, 1),
        }
    )

    network.add_road("A", "B", 2)
    network.add_road("B", "C", 2)
    network.add_road("A", "D", 1)
    network.add_road("D", "C", 10)

    assert network.fastest_route("A", "C") == (4, ["A", "B", "C"])

    network.update_travel_time("D", "C", 1)
    assert network.fastest_route("A", "C") == (2, ["A", "D", "C"])

    print("All tests passed!")

