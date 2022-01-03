# BFS na listach sąsiedztwa. Najkrótsze ścieżki w grafie nieważonym

from queue import Queue


def BFS(G, s):
    V = len(G)
    Q = Queue()
    visited = [False] * V
    results = [None] * V

    results[s] = (None, 0)  # krotka (parent, distance_from_source)
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in range(len(G[u])):
            if not visited[G[u][v]]:
                visited[G[u][v]] = True
                results[G[u][v]] = (u, results[u][1] + 1)
                Q.put(G[u][v])
    return results


G = [[1, 2, 3],
     [0, 3, 4],
     [0, 3, 4],
     [0, 1, 2, 4],
     [1, 2, 3]]

print(BFS(G, 0))