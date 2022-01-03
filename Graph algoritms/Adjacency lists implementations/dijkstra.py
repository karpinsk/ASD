# Algorytm Dijkstry dla list sąsiedztwa. Najkrótsze ścieżki w grafie ważonym 1-to-all

from queue import PriorityQueue


def dijkstra_lists(G, s):
    V = len(G)
    Q = PriorityQueue()
    d = [float("inf")] * V
    parents = [None] * V
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        u = Q.get()
        for v in range(0, len(G[u[1]])):
            if d[G[u[1]][v][0]] > d[u[1]] + G[u[1]][v][1]:  # relaksacje
                d[G[u[1]][v][0]] = d[u[1]] + G[u[1]][v][1]
                parents[G[u[1]][v][0]] = u[1]
                Q.put((d[G[u[1]][v][0]], G[u[1]][v][0]))
            print(parents)
    return d


G_lists = [[(1, 7), (2, 3)], [(3, 15)], [(1, 2), (3, 8)], []]
print(dijkstra_lists(G_lists, 0))