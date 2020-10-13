# Give a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

# DEFINITION
# Circular linked listL A (corrput) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

# EXAMPLE
# Input  A - > B -> C -> D - > E -> C [the same C as earlier]
# Output C

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def fill(self, nodes):
        for node in nodes:
            self.append(node)

# Solution
# Floyd's tortoise and hare
# Time Complexity: O(n)
# Space Complexity: O(1)
def has_loop(ll):
    slow = ll.head
    fast = ll.head
    while fast:
        slow = slow.next
        if fast.next:
            # This is for when the linked list doesn't have a loop
            fast = fast.next.next
        if fast == slow:
            fast = ll.head
            while True:
                if fast == slow:
                    print(fast.data)
                    return True
                fast = fast.next
                slow = slow.next
    return False

# Replicating the following
# 1 -> 2 -> 3
#         /  \
#       5 <-- 4

ll = LinkedList()
repeated_node = Node(3)
ll.fill([Node(1), Node(2), repeated_node, Node(4), Node(5), repeated_node])
print(has_loop(ll))

another_ll = LinkedList()
repeated_node = Node(3)
another_ll.fill([Node(1), Node(2), Node(4), Node(5)])
print(has_loop(another_ll))
