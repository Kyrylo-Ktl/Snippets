"""Construction of a minimum spanning tree by Kraskal's algorithm"""

from DataStructures.Other.DSU import DSU


def kruskals(n: int, g_from: list, g_to: list, weights: list) -> int:
    """Implementation of the Kraskal algorithm using DSU

    Time:   O(n*log(n))
    Memory: O(n)
    """
    dsu = DSU(n + 1)
    cost = 0

    for w, u, v in sorted(zip(weights, g_from, g_to)):
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            cost += w

    return cost
