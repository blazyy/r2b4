import random
import timeit

'''
Hybrid quicksort is where when the partitions get to a certain short
length, let's say 10 elements, instead of doing quicksort on these
we do an insertion sort instead. This is more efficient since
insertion sort is faster than quicksort for smaller arrays since
the number of comparisons and swaps being done is comparatively lesser.
'''


def partition(arr, start, end):
    p_index = start
    pivot = arr[end]
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


def insertion_sort(arr, start, end):
    for i in range(start+1, end):
        current = i
        value = arr[current]
        while current > start and arr[current-1] > value:
            arr[current] = arr[current-1]
            current -= 1
        arr[current] = value


def hybrid_quick_sort(arr, start, end):
    # Insertion sort only if there are fewer than 11 elements in the partition
    if end-start <= partition_limit:
        insertion_sort(arr, start, end)
    else:
        if start < end:
            p_index = partition(arr, start, end)
            hybrid_quick_sort(arr, start, p_index - 1)
            hybrid_quick_sort(arr, p_index + 1, end)


def bubble_sort(arr, size):
    for i in range(size):
        for j in range(size - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


partition_limit = 10
dp = 4
n_tests = 10
size = 10000


def quick_sort_time(size=size):
    arr = [random.randint(1, 1000) for i in range(size)]
    quick_sort(arr, 0, size-1)


def hybrid_quick_sort_time(size=size):
    arr = [random.randint(1, 1000) for i in range(size)]
    hybrid_quick_sort(arr, 0, size-1)


def built_in_sort_time(size=size):
    arr = [random.randint(1, 1000) for i in range(size)]
    sorted(arr)


t1 = timeit.Timer('quick_sort_time(size)',
                  'from __main__ import quick_sort_time, \
                   quick_sort, partition, partition_limit, size')
t2 = timeit.Timer('hybrid_quick_sort_time(size)',
                  'from __main__ import hybrid_quick_sort_time, \
                   hybrid_quick_sort, partition, partition_limit, size')
t3 = timeit.Timer('built_in_sort_time(size)',
                  'from __main__ import built_in_sort_time, size')

print('QuickSort:\t\t{} ms'.format(round(t1.timeit(n_tests), dp)))
print('Hybrid QuickSort:\t{} ms'.format(round(t2.timeit(n_tests), dp)))
print('Built-in Sort:\t\t{} ms'.format(round(t3.timeit(n_tests), dp)))


'''
On a list of size 10000 running for 1000 tests, I got the following results:

QuickSort:              88.2298 ms
Hybrid QuickSort:       71.0913 ms
Built-in Sort:          21.9112 ms

As expected, hybrid quicksort performs faster on very large arrays.
But the built-in sort beats them by many miles.
Python's built-in sort an implementation of timsort developed in 2002.
It's a hybrid sort algorithm which uses a combination of
merge sort + insertion sort.

'''
