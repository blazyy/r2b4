# Page 49

# Giveen two sorted arrays, find the number of elements in commong. Arrays are of same length and each array has distinct elements.
A = [13, 27, 35, 40, 49, 55, 59]
B = [17, 35, 39, 40, 55, 58, 60]

# Naive Solution - O(n^2) time and O(1) space
def naive():
    common = []
    for a in A:
        for b in B:
            if a == b:
                common.append(a)
    print(common)

# Suboptimal Solution - O(n log n) time, O(1) space
def suboptimal_1():
    def binary_search(arr, start, end, ele):
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] == ele:
                return True
            elif arr[mid] > ele:
                end = mid - 1
            else:
                start = mid + 1
        return False
    common = []
    for a in A:
        if binary_search(B, 0, len(B) - 1, a):
            common.append(a)
    print(common)

# Suboptimal Solution - O(n) time, O(n) space
def suboptimal_2():
    hashmap = {}
    common = []
    for a in A:
        hashmap[a] = ' '
    for b in B:
        if b in hashmap:
            common.append(b)
    print(common)

# Optimal Solution - O(n) time, O(1) space
def optimal():
    ptr = 0
    common = []
    for a in A:
        if a < B[ptr]:
            continue
        elif a > B[ptr]:
            ptr += 1
        else:
            common.append(a)
    print(common)


naive()
suboptimal_1()
suboptimal_2()
optimal()
