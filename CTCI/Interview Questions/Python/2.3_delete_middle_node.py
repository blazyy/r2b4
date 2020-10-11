# Implement an algorithm to delete a node in the midddle (i.e. any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node

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
# Starting from the middle (because that's all we have access to), copy the data from the next node (if it exists) and set it to the node before it.
# Time Complexity: O(n), Space Complexity: O(1)
def delete_middle_node(mid_node):
    while mid_node.next:
        mid_node.data = mid_node.next.data
        if mid_node.next.next is None:
            mid_node.next = None
            break
        mid_node = mid_node.next

num_nodes = 10
ll = LinkedList()
ll.fill([random.randint(1, num_nodes) for i in range(num_nodes)])
print(ll)

mid_node = ll.head
i = 1
while i < num_nodes//2:
    i += 1
    mid_node = mid_node.next
print('Removing middle node ({})'.format(mid_node.data))
delete_middle_node(mid_node)
print(ll)
