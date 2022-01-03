class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)  # kompresja ścieżki
    return x.parent  # tu korzystamny z tego że parentem roota jest root


def union(x, y):
    x = find(x)
    y = find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
