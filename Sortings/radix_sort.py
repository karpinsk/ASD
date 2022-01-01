def radix_sort(arr):
    max_el = max(arr)
    exp = 1
    while max_el/exp > 0:
        counting_sort(arr, exp)  
        exp *= 10


def counting_sort(arr, k):
    n = len(arr)
    result_arr = [0] * n
    count_arr = [0] * 10
    for i in range(n):
        index = arr[i] // k
        count_arr[index % 10] += 1
    for i in range(1, 10):
        count_arr[i] += count_arr[i-1]      # how many elements are less or equal than i
    for i in range(n-1, -1, -1):
        index = arr[i] // k
        count_arr[index % 10] -= 1
        result_arr[count_arr[index % 10]] = arr[i]
    for i in range(n):
        arr[i] = result_arr[i]


tab = [45153114, 11, 2, 73, 3301, 911, 14, 0, 404, 1, 0, 1]
radix_sort(tab)
print(tab)