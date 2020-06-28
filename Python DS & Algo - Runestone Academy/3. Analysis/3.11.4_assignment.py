# Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.

import random

def kth_smallest_number(lst, k):
    lst.sort()
    return lst[k]

lst = [random.randrange(1, 100) for i in range(10)]
k = 1


print('Unsorted list: {}'.format(lst))
lst.sort()
print('Sorted list: {}'.format(lst))
print("k = {}, number = {}".format(k, kth_smallest_number(lst, k)))
