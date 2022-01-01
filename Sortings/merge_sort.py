def merge_sort(arr):
    if len(arr) == 1:
        return arr
    pivot = len(arr) // 2
    left = arr[0:pivot]
    right = arr[pivot:len(arr)]
    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
merge_sort(tab)
print(tab)