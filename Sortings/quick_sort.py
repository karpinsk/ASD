def quick_sort(arr, p, r):
    while p < r:
        m = partition(arr, p, r)
        if (m-p) > (r - m):             # we make recursive calls only for bigger parts
            quick_sort(arr, p, m-1)
            p = m
        else:
            quick_sort(arr, m, r)
            r = m-1


def partition(arr, p, r):
    pivot = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
quick_sort(tab, 0, len(tab)-1)
print(tab)