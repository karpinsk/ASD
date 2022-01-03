# Algorytm DFS na macierzy sąsiedztwa. Najkrótsze ścieżki w grafie nieważonym


def DFS(G):
    def DFSVisit(G, u, time):
        time += 1
        visited[u] = True
        entry[u] = time
        for v in range(V):
            if not visited[v] and G[u][v] == 1:
                parent[v] = u
                time = DFSVisit(G, v, time)
        time += 1
        processed[u] = time
        return time

    V = len(G)
    # results = [None] * V  # uzupelniamy zaleznie od tego co chcemy zwrocic (jakies krotki czy cos)
    visited = [False] * V
    parent = [None] * V
    entry = [0] * V
    processed = [0] * V
    time = 0
    for v in range(V):
        if not visited[v]:
            time = DFSVisit(G, v, time)
    return parent, entry, processed


G_matrix = [[0, 1, 1, 0], [0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 0]]
parent, entry, processed = DFS(G_matrix)
print("(parent, ", "entry, ", "processed)")
print(parent, entry, processed)
