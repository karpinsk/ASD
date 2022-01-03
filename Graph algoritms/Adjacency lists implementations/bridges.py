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

        for i in range(len(G[u])):
            v = G[u][i]

            if not visited[v]:
                parents[v] = u
                visited[v] = True
                DFSvisit(v)

                low[u] = min(low[u], low[v])

            elif visited[v] and parents[u] != v:
                low[u] = min(low[u], entry[v])

    for v in range(V):
        if not visited[G[v][0]]:
            DFSvisit(G[v][0])

    bridges = []

    for i in range(V):
        if entry[i] == low[i] and parents[i] is not None:
            bridges.append((parents[i], i))

    return bridges


G = [[1, 2],
     [0, 3],
     [0, 3],
     [1, 2, 4],
     [3, 5, 7],
     [4, 6],
     [5, 7],
     [4, 6]]

bridges = DFS(G)
print("bridges: ", bridges)
