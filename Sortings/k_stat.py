import random

def random_partition(arr, p, r):
    ind = random.randint(p, r)
    arr[ind], arr[r] = arr[r], arr[ind]
    return partition(arr, p, r)

def partition(arr, p, r):
    pivot = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def random_select(arr, p, r, i):
    if p == r:
        return arr[p]
    q = random_partition(arr, p, r)
    k = q-p+1
    if i == k:
        return arr[q]
    elif i < k:
        return random_select(arr, p, q-1, i)
    return random_select(arr, q+1, r, i-k)


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
print(random_select(tab, 0, len(tab)-1, 7))