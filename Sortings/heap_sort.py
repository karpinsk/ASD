def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(arr, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, i, n)

def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr) - 1
    heap_size = n
    for i in range(n, 1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, 0, heap_size)
    return arr


tab = [45153114, 11, 2, 73, 3301, 911, -1, 0, 404, 1, 0, 1]
print(heap_sort(tab))