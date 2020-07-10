import random
import timeit


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


def quick_sort_randomized(arr, start, end):
    if start < end:
        rand_pivot = random.randint(start, end-1)
        arr[rand_pivot], arr[end-1] = arr[end-1], arr[rand_pivot]
        value = arr[end-1]
        p_index = start
        for i in range(start, end):
            if arr[i] < value:
                arr[p_index], arr[i] = arr[i], arr[p_index]
                p_index += 1
        arr[p_index], arr[end-1] = arr[end-1], arr[p_index]
        quick_sort(arr, start, p_index)
        quick_sort(arr, p_index + 1, end)


def quick_sort_time(size=1000):
    for i in range(size):
        arr = [random.randint(1, 100) for i in range(size)]
        quick_sort(arr, 0, size)


def quick_sort_randomized_time(size=1000):
    for i in range(size):
        arr = [random.randint(1, 100) for i in range(size)]
        quick_sort_randomized(arr, 0, size)


t1 = timeit.Timer('quick_sort_time(size)',
                  'from __main__ import quick_sort_time, size')
t2 = timeit.Timer('quick_sort_randomized_time(size)',
                  'from __main__ import quick_sort_randomized_time, size')


size = 100
n_tests = 1000
dp = 6
print('Quick Sort:\t\t', round(t1.timeit(n_tests), dp))
print('Quick Sort Randomized:\t', round(t2.timeit(n_tests), dp))


'''
On an array of size 100 with 1000 tests:

Quick Sort:              44.203724
Quick Sort Randomized:   37.811918
'''
