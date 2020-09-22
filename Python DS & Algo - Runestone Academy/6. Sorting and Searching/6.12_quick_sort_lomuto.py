import random


def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1
    arr[p_index], arr[end] = arr[end], arr[p_index]
    return p_index


def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index - 1)
        quick_sort(arr, p_index + 1, end)


size = 16
arr = [random.randint(1, 100) for i in range(size)]
print(arr)
quick_sort(arr, 0, size-1)
print(arr)
