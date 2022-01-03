# all-to-all najkrótsze ścieżki
# WYMAGA MACIERZY SĄSIEDZTWA


def floyd_warshall(G):
    V = len(G)
    d = [[float("inf") for _ in range(V)] for _ in range(V)]  # tablica 2-wymiarowa nieskonczonosci
    p = [[None for _ in range(V)] for _ in range(V)]  # p[i][j] = t oznacza ze najkrotsza sciezka z i do j przechodzi
                                                      # przez t
    for i in range(0, V):
        for j in range(0, V):
            if i == j:
                d[i][j] = 0
            elif G[i][j] is not None:
                d[i][j] = G[i][j]
    for t in range(0, V):
        for i in range(0, V):
            for j in range(0, V):
                tmp = d[i][j]
                d[i][j] = min(d[i][j], d[i][t] + d[t][j])
                if d[i][j] != tmp:
                    p[i][j] = t
    # zwracamy odleglosci i tablice pomocnicza
    return d, p


# ---------------------------------------------------
# Funkcje pomocnicze

# przyjmuje tablice z wierzcholkiem startowym
# zwraca sciezke
def get_path_help(p, result, i, j):
    if p[i][j] is None:  # sciezka ma dlugosc 1
        result.append(j)
    else:
        get_path_help(p, result, i, p[i][j])
        get_path_help(p, result, p[i][j], j)
    return result


# zwraca tablice wierzcholkow które są kolejnymi
# przystankami sciezki z wierzcholka i do j
def get_path(p, i, j):
    result = [i]
    result = get_path_help(p, result, i, j)
    return result


G = [[None, 5, 3, None],
     [5, None, 1, 2],
     [3, 1, None, 7],
     [None, 2, 7, None]]

d, p = floyd_warshall(G)
print(get_path(p, 0, 3))
print(d)