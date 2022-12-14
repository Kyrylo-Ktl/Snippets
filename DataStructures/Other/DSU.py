"""Module with the implementation of the system of disjoint sets (DSU)"""

from random import randint


class DSU:
    """
    Disjoint set system with rank and path compression heuristics

    Memory:
        creation - O(n)
        'find' - O(log(n))
        'union' - O(log(n))

    Time:
        creation - O(n)
        'find' - O(log(n))
        'union' - O(log(n))

    On average, operations 'find' and 'union' take O(1) time and space
    """

    def __init__(self, size: int):
        self.parent = [p for p in range(size)]
        self.rank = [1 for _ in range(size)]

    def find(self, a: int) -> int:
        if a != self.parent[a]:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a: int, b: int):
        a_root = self.find(a)
        b_root = self.find(b)

        if a_root == b_root:
            return

        if self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = a_root
        elif self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = b_root
        else:
            if randint(0, 1) & 1:
                a_root, b_root = b_root, a_root
            self.parent[b_root] = a_root
            self.rank[a_root] += 1
