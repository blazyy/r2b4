# Given two singly linked list, determine if two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) and the jth node of the second linked list, then they are intersecting.

# Page 64

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def fill(self, elements):
        for element in elements:
            self.append(element)

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return ' '.join([str(ele) for ele in elements])

# Solution
# Traverse both lists at same speed. When we reach the end of the shorter list, it is set to the head of the longer list. When we reach the end of the longer list, we set it to the head of the shorter list. At this point, the two pointers are n nodes between each other where n is the difference in their size. (If both lists are the same size, they will intersect even before starting from the heads again) After they have been set to the respective heads, traversing the list normally will reach a point where both will meet at the same node (if intersection exists)
# To check for no intersection, just check if the tail nodes of each list are equal. If they aren't, there is no intersection.
# Time Complexity: O(m + n) where m and n are the sizes of each of the lists.
# Space Complexity: O(1)
def are_intersecting(list_a, list_b):
    curr_a = list_a.head
    curr_b = list_b.head
    if curr_a is None or curr_b is None:
        return False
    tail_a = None
    tail_b = None
    while True:
        # Lists which do not intersect have different tails
        if tail_a and tail_b and tail_a != tail_b:
            return False
        if curr_a == curr_b:
            return True
        if curr_a.next:
            curr_a = curr_a.next
        else:
            tail_a = curr_a
            curr_a = list_b.head
        if curr_b.next:
            curr_b = curr_b.next
        else:
            tail_b = curr_b
            curr_b = list_a.head

# Creating the following list:

#   3 -> 1 -> 5 -> 9
#                   \
#                    7 -> 2 -> 1
#           4 -> 6 /

intersecting_node = Node(7)

list_a = LinkedList()
list_a.fill([Node(3), Node(1), Node(5), Node(9)])
list_a.append(intersecting_node)
list_a.fill([Node(2), Node(1)])

list_b = LinkedList()
list_b.fill([Node(4), Node(6)])
list_b.append(intersecting_node)

print(are_intersecting(list_a, list_b))

list_b = LinkedList()
list_b.fill([Node(4), Node(6), Node(7)])
print(are_intersecting(list_a, list_b))
