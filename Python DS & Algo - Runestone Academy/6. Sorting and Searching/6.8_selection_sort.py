import random


def selection_sort(lst):
    for i in range(len(lst)-1, -1, -1):
        idx_max = lst.index(max(lst[:i+1]))
        lst[idx_max], lst[i] = lst[i], lst[idx_max]
    return lst


lst = [random.randint(1, 100) for i in range(10)]
print(lst)
sorted_lst = selection_sort(lst)
print(sorted_lst)
