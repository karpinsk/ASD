# W implementacji na listach wystarczy sprawdzić długości list: muszą być parzyste i większe od 0


def euler(G):
    def DFSVisit(u, time):
        time += 1
        entry[u] = time
        for v in range(V):
            if G[u][v] == 1:
                parent[v] = u
                G[u][v] = 0  # USUWAMY KRAWĘDŹ
                G[v][u] = 0
                DFSVisit(v, time)
        time += 1
        processed[u] = time
        results.append(u)

    V = len(G)
    results = []
    parent = [None] * V
    entry = [0] * V
    processed = [0] * V
    time = 0
    DFSVisit(0, time)
    return results


G_matrix = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]
euler_cycle = euler(G_matrix)
print(euler_cycle)
