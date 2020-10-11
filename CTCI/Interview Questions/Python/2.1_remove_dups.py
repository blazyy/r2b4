# Write code to remove duplicates from an unsorted linked list

# Page 63

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    def __str__(self):
        output_list = []
        current = self.head
        while current:
            output_list.append(current.data)
            current = current.next
        return ' '.join([str(ele) for ele in output_list])

# Solution 1
# Use set to store visited elements
# Time Complexity: O(n), Space Complexity: O(n)
def remove_dups_1(ll):
    if ll is None or ll.head is None:
        return None
    visited = set()
    current = ll.head
    prev = current
    while current:
        if current.data in visited:
            prev.next = current.next
        else:
            prev = current # Only change previous if not a duplicate, because after setting prev.next to current.next, prev should stay at prev and not move to prev.next which is the current deleted node.
            visited.add(current.data)
        current = current.next

# Solution 2
# Once at a node, traverse through the remaining right part of the linked list and remove if that node's value is seen again
# Time Complexity: O(n^2), Space Complexity: O(1)
def remove_dups_2(ll):
    current = ll.head
    while current:
        prev = current
        traverser = current.next
        while traverser:
            if traverser.data == current.data:
                prev.next = traverser.next
            else:
                prev = traverser # Only change previous if not a duplicate, because after setting prev.next to current.next, prev should stay at prev and not move to prev.next which is the current deleted node.
            traverser = traverser.next
        current = current.next


ll = LinkedList()
ll.fill([random.randint(1, 10) for i in range(20)])
print(ll)
remove_dups_1(ll)
print(ll)

print()

ll = LinkedList()
ll.fill([random.randint(1, 10) for i in range(20)])
print(ll)
remove_dups_2(ll)
print(ll)
