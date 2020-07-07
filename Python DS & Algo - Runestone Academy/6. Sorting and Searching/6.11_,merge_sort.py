import random

# The code is not very pythonic. Will change in the future.


def merge(left, lsize, right, rsize, arr, size):
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


def merge_sort(arr, size):
    if size < 2:
        return
    mid = size // 2
    lsize = mid
    rsize = size - mid
    left = []
    right = []
    for i in range(mid):
        left.append(arr[i])
    for i in range(mid, size):
        right.append(arr[i])
    merge_sort(left, lsize)
    merge_sort(right, rsize)
    merge(left, lsize, right, rsize, arr, size)


size = 10
arr = [random.randint(1, 100) for i in range(size)]
print(arr)
merge_sort(arr, size)
print(arr)
