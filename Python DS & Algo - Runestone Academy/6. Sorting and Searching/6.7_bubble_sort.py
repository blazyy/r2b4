import random


def bubble_sort(lst):
    for i in range(len(lst)):
        swapped = False
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True  # Returns if list has been sorted
        if not swapped:
            return lst
    return lst


lst = [random.randint(1, 100) for i in range(10)]
print(lst)
sorted_lst = bubble_sort(lst)
print(sorted_lst)
