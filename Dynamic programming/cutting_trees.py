# f(i) - maksymalny zysk zcięcia do i-tego drzewa

# f(i) = max (f(i-2) + value[i], f(i-1))

def lumberjack(trees):
    n = len(trees)
    x2 = trees[0]
    x1 = max(trees[0], trees[1])
    for i in range(2, n):
        x1, x2 = max(x2 + trees[i], x1), x1
    return x1


arr = [5, 1, 12, 14, 2, 2, 2, 19, 1, 7]
print(lumberjack(arr))
