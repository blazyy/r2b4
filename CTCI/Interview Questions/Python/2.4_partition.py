# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see example below). The partition element x can appear anywhere in the "right partition". It does not need to appear between the left and right partitions.

# Input  = 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# Output = 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

# Page 64

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

# Solution
# This can be solved with the partitioning scheme used in quicksort. In this case, it only needs to be called once.
# Time Complexity: O(n), Space Complexity: O(1)
def partition(ll, pivot):
    p_index = ll.head
    current = ll.head
    while current:
        if current.data < pivot:
            temp = current.data
            current.data = p_index.data
            p_index.data = temp
            p_index = p_index.next
        current = current.next

ll = LinkedList()
elements = [random.randint(1, 10) for i in range(8)]
ll.fill(elements)
print(ll)
pivot = sorted(elements)[len(elements)//2] # Choosing the middle element of sorted elements that were appeneed to the linked list.
print(' '.join([str(ele) for ele in sorted(elements)]))
print('Pivot: ', pivot)
partition(ll, pivot)
print(ll)
