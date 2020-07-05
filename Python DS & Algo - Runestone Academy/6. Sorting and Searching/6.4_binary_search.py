def binary_search(lst, ele, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if lst[mid] == ele:
        return True
    elif lst[mid] > ele:
        return binary_search(lst, ele, start, mid - 1)
    else:
        return binary_search(lst, ele, mid + 1, end)


lst = [1, 3, 5, 7, 9, 11, 13]
ele = 94
print(binary_search(lst, ele, 0, len(lst)-1))
