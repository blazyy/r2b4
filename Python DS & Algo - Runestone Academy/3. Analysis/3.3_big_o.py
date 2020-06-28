# Write two Python functions to find the minimum number in a list. The first function should compare each number to every other number on the list. O(n2). The second function should be linear O(n).

def find_min_linear(lst):
    smallest_num = lst[0]
    for num in lst:
        if num < smallest_num:
            smallest_num = num
    return smallest_num
