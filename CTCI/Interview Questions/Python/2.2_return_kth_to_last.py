# Implement an algorithm to find the kth to last element of a singly linked list

# Page 63

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def fill(self, elements):
        for element in elements:
            self.append(element)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        self.size += 1

    def __str__(self):
        output_list = []
        current = self.head
        while current:
            output_list.append(current.data)
            current = current.next
        return ' '.join([str(ele) for ele in output_list])

# Solution 1
# Traverse through list until index (n-k) is visited.
# This solution assumes size of list is already known.
# Time Complexity: O(n), Space Complexity: O(1)
def return_kth_to_last_1(ll, k):
    kth_to_last_idx = ll.size - k
    idx = 0
    current = ll.head
    while current:
        if idx == kth_to_last_idx:
            return current.data
        idx += 1
        current = current.next

# Solution 2
# Recursive solution - doesn't return kth-from-last, only prints.
# List size not known.
# Time Complexity: O(n), Space Complexity: O(n) (since recursive)
def return_kth_to_last_2(node, k):
    if node is None:
        return 0
    index = return_kth_to_last_2(node.next, k) + 1
    if index == k:
        print(node.data)
    return index

# Solution 3
# Iterative - size of list unknown. Instead of two passes(one for finding size and then one for finding kth-to-last), do in one pass
# Time Complexity: O(n), Space Complexity: O(1)
def return_kth_to_last_3(ll, k):
    idx = 1 # Considering last element as index 1 (instead of 0) when read in reverse
    fast = ll.head
    slow = None
    while fast:
        if slow is not None:
            slow = slow.next
        if idx == k:
            slow = ll.head
        if fast.next is None:
            return slow.data
        idx += 1
        fast = fast.next
ll = LinkedList()
ll.fill([random.randint(1, 10) for i in range(20)])
print(ll)
print(return_kth_to_last_1(ll, 3))
return_kth_to_last_2(ll.head, 5)
print(return_kth_to_last_3(ll, 3))
