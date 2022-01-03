# Algorytm Dijkstry dla macierzy sąsiedztwa. Najkrótsze ścieżki w grafie ważonym 1-to-all

from queue import PriorityQueue


def dijkstra_matrix(G, s):
    V = len(G)
    Q = PriorityQueue()
    d = [float("inf")] * V
    parents = [None] * V
    d[s] = 0
    Q.put((d[s], s))

    while not Q.empty():
        u = Q.get()
        for v in range(V):
            if G[u[1]][v] is not None and d[v] > d[u[1]] + G[u[1]][v]:
                d[v] = d[u[1]] + G[u[1]][v]
                parents[v] = u[1]
                Q.put((d[v], v))
    #     print(parents)
    return d


G_matrix = [[None, 7, 3, None], [None, None, None, 15], [None, 2, None, 8], [None, None, None, None]]
print(dijkstra_matrix(G_matrix, 0))