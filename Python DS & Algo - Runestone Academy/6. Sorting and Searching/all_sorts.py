import random


def generate_array(size):
    return [random.randint(1, 100) for i in range(size)]


def bubble_sort(arr, size):
    for i in range(size):
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr, size):
    last_idx = size - 1
    for i in range(size):
        max_idx = arr.index(max(arr[:last_idx+1]))
        arr[last_idx], arr[max_idx] = arr[max_idx], arr[last_idx]
        last_idx -= 1


def insertion_sort(arr, size):
    for i in range(1, size):
        current = i
        value = arr[i]
        while arr[current-1] > value and current > 0:
            arr[current] = arr[current-1]
            current -= 1
        arr[current] = value


def merge_sort(arr, size):
    if size < 2:
        return
    mid = size // 2
    lsize = mid
    rsize = size - mid
    left = arr[:mid]
    right = arr[mid:size]
    merge_sort(left, lsize)
    merge_sort(right, rsize)
    l_idx = r_idx = idx = 0
    while l_idx < lsize and r_idx < rsize:
        if left[l_idx] <= right[r_idx]:
            arr[idx] = left[l_idx]
            l_idx += 1
        else:
            arr[idx] = right[r_idx]
            r_idx += 1
        idx += 1
    while l_idx < lsize:
        arr[idx] = left[l_idx]
        idx += 1
        l_idx += 1
    while r_idx < rsize:
        arr[idx] = right[r_idx]
        idx += 1
        r_idx += 1


def quick_sort(arr, start, end):
    if start < end:
        pivot = end-1
        value = arr[pivot]
        p_index = start
        for i in range(start, end):
            if arr[i] < value:
                arr[p_index], arr[i] = arr[i], arr[p_index]
                p_index += 1
        arr[p_index], arr[pivot] = arr[pivot], arr[p_index]
        quick_sort(arr, start, p_index)
        quick_sort(arr, p_index + 1, end)


size = 10
arr = generate_array(size)
print(arr)
quick_sort(arr, 0, size)
print(arr)
