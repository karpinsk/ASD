def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j > -1 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
insertion_sort(tab)
print(tab)