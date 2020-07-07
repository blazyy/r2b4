import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = i
        value = arr[i]
        while current > 0 and arr[current-1] > value:
            arr[current] = arr[current - 1]
            current = current - 1
        arr[current] = value
    return arr


arr = [random.randint(1, 100) for i in range(10)]
print(arr)
sorted_arr = insertion_sort(arr)
print(sorted_arr)
