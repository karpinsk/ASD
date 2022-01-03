time = 0


def DFS(G):
    V = len(G)
    visited = [False] * V
    parents = [None] * V
    entry = [None] * V
    low = [None] * V

    def DFSvisit(u):
        global time
        time += 1
        entry[u] = time
        low[u] = time
        visited[u] = True

        for i in range(V):
            if not visited[i] and G[u][i] == 1:
                parents[i] = u
                visited[i] = True
                DFSvisit(i)

                low[u] = min(low[u], low[i])

            elif visited[i] and G[u][i] == 1 and parents[u] != i:

                low[u] = min(low[u], entry[i])

    for v in range(V):
        for k in range(V):
            if not visited[G[v][k]]:
                DFSvisit(G[v][k])

    bridges = []

    for i in range(V):
        if entry[i] == low[i] and parents[i] is not None:
            bridges.append((parents[i], i))

    return bridges



G = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 1, 1],
     [0, 0, 0, 0, 1, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0]]

bridges = DFS(G)
print("bridges: ", bridges)
