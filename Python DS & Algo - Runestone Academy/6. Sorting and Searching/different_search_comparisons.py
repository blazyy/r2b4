import random
import timeit


def sequential_search(arr, ele):
    for num in arr:
        if num == ele:
            return True
    return False


def binary_search_recursive(arr, ele, start, end):
    if start > end:
        return False
    mid = (end + start) // 2
    if arr[mid] == ele:
        return True
    elif arr[mid] >= ele:
        return binary_search_recursive(arr, ele, start, mid - 1)
    else:
        return binary_search_recursive(arr, ele, mid + 1, end)
    return False


def binary_search_iterative(arr, ele, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == ele:
            return True
        elif arr[mid] >= ele:
            end = mid - 1
        else:
            start = mid + 1
    return False


def seq_search_time(arr, lb=1, ub=100):
    sequential_search(arr, random.randint(lb, ub))


def bin_search_rec_time(arr, size, lb=1, ub=100):
    binary_search_recursive(arr, random.randint(lb, ub), 0, size-1)


def bin_search_iter_time(arr, size, lb=1, ub=100):
    binary_search_iterative(arr, random.randint(lb, ub), 0, size-1)


n_tests = 100
dp = 6
arr = [i for i in range(1000000) if i % 2 == 0]  # even numbers
size = len(arr)

t1 = timeit.Timer('seq_search_time(arr)',
                  'from __main__ import seq_search_time, arr')
t2 = timeit.Timer('bin_search_rec_time(arr, size)',
                  'from __main__ import bin_search_rec_time, arr, size')
t2 = timeit.Timer('bin_search_iter_time(arr, size)',
                  'from __main__ import bin_search_iter_time, arr, size')

print('List Size:\t\t', size, sep='')
print('Seq. Search:\t\t{} ms'.format(round(t1.timeit(number=n_tests), dp)))
print('Bin. Rec.Search:\t{} ms'.format(round(t2.timeit(number=n_tests), dp)))
print('Bin. Iter. Search:\t{} ms'.format(round(t2.timeit(number=n_tests), dp)))

'''
Initially I was surprised why sequential search was showing faster runtimes.
Then I realized I was using small arrays for searching.
For smaller lists, upto 125 elements in size, sequential performs better.
In real life, you never work with numbers that low.
So yeah, binary search FTW.

As for iterative vs. recursive binary search, I did not see much difference
in performance. Usually, recursive binary search has more overhead due to the
call stack. This means it uses O(log N) space compared to iterative which uses
O(1) space. However modern compilers convert these 'tail-recursions' to
iterative versions.A tail-recursion is where the recursive function call is the
last line to execute in a function.
Due to them converting these tail-recursions to iterative versions,
the difference in performance was non-negligible, atleast according
to my experiments.
'''
