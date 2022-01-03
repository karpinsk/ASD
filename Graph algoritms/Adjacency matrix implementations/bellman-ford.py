# Algorytm Bellmana-Forda dla znalezienia najkrótszych ścieżek od startowego do wszystkich. Graf może mieć wagi ujemne


def bellman_ford(G, s):
    V = len(G)
    d = [float("inf")] * V
    parent = [None] * V
    d[s] = 0
    for u in range(V):
        for v in range(V):
            if G[u][v] is not None and d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                parent[v] = u

    # sprawdzenie ujemnego cyklu
    for u in range(V):
        for v in range(V):
            if G[u][v] is not None and d[v] > d[u] + G[u][v]:
                return False  # cykl ujemny
    print(parent)
    return d


G_matrix = [[None, 7, 3, None], [None, None, None, 15], [None, 2, None, 8], [None, None, None, None]]
print(bellman_ford(G_matrix, 0))