def bucket_sort(arr, low, high):
    n = len(arr)
    res = []
    buckets = [[] for i in range(n)]
    width = (high - low) / n
    for i in range(n):
        number = int(arr[i]/width)
        buckets[number].append(arr[i])
    for i in range(len(buckets)):
        insertion_sort(buckets[i])
    for i in range(len(buckets)):
        res.extend(buckets[i])
    return res

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j > -1 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


tab = [0.1, 0.11, 0.78, 0.91, 0.37, 0.21, 0.55, 0.81, 0.74]
print(bucket_sort(tab, 0, 1))