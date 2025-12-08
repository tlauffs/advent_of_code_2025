from collections import defaultdict
import math
from typing import DefaultDict

class Vector_3d:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def distance_euclidean(self, other: "Vector_3d") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2 +
            (self.z - other.z) ** 2
        )

class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> None|bool:
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        self.parents[x_root] = y_root
        self.sizes[y_root] += self.sizes[x_root]
        if self.sizes[y_root] == len(self.parents):
            return True
        return False

    def cluster_sizes(self) -> DefaultDict[int, int]:
        counts: DefaultDict[int,int] = defaultdict(int)
        for i in range(len(self.parents)):
            root = self.find(i)
            counts[root] += 1
        return counts

junctions: list[Vector_3d] = []
with open("input.txt") as f:
    for line in f.readlines():
        junctions.append(Vector_3d(*map(int, line.split(','))))

edges = []
for i in range(len(junctions)):
    for j in range(i+1, len(junctions)):
        dist = junctions[i].distance_euclidean(junctions[j])
        edges.append((dist, i, j))

edges.sort(key=lambda x: x[0])
shortest_1000 = edges[:1000]

union = UnionFind(len(junctions))
for dist, i, j in shortest_1000:
    union.union(i, j)

cluster_sizes = union.cluster_sizes()
sizes = sorted(cluster_sizes.values(), reverse=True)

print(f"Part 1: {sizes[0] * sizes[1] * sizes[2]}")

after_1000 = edges[1000:]
for dist, i, j in after_1000:
    last_connection = union.union(i, j)
    if last_connection:
        cable_dist_needed = junctions[i].x * junctions[j].x
        print(f"Part 2: {cable_dist_needed}")
        break
