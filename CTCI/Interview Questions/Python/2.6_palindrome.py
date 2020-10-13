# Implement a function to check if a linked list is a palindrome.

# Page 64

import copy # For creating an object copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def fill(self, elements):
        if self.head:
            self.head = None # Doing this just to make the main function cleaner
        for element in elements:
            self.append(element)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def set_head(self, new_head):
        self.head = new_head

    def __str__(self):
        output_list = []
        current = self.head
        while current:
            output_list.append(current.data)
            current = current.next
        return ' '.join([str(ele) for ele in output_list])

# Solution 1
# Using a stack store store the first half of the palindrome, then popping each and checking with latter half of linked list.
# Solution assumes that size of linked list is not known.
# Time Complexity: O(n), Space Complexity: O(n)
def is_palindrome_1(ll):
    # If string is less than 1 character long
    if ll.head is None or ll.head.next is None:
        return True
    # If string is two characters long
    if ll.head.data == ll.head.next.data and ll.head.next.next is None:
        return True
    slow = ll.head
    fast = ll.head
    stack = []
    while True:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
        # If character has an odd number of characters
        if fast.next is None:
            slow = slow.next
            break
        # If character has an even number of characters
        elif fast.next is not None and fast.next.next is None:
            stack.append(slow.data)
            slow = slow.next
            break
    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True

def reverse_and_clone_ll(ll):
    rev_ll = copy.deepcopy(ll) # Cloning linked list. Deep copy means changes to the copied-from linked list won't have any effect on the copied linked list.
    current = rev_ll.head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    rev_ll.set_head(prev)
    return rev_ll

def compare_linked_lists(ll, rev_ll):
    first = ll.head
    second = rev_ll.head
    fast = ll.head
    # Since we're looking for palindromes, traversing through the entire list isn't necessary. We stop when we're at the halfway point.
    while first and second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
        if fast.next and fast.next.next:
            fast = fast.next.next
        else:
            break
    return True

# Solution 2
# Reversing linked list and check first half of each list
# Time Complexity: O(n), Space Complexity: O(n)
def is_palindrome_2(ll):
    rev_ll = reverse_and_clone_ll(ll)
    return compare_linked_lists(ll, rev_ll)


ll = LinkedList()
ll.fill([ch for ch in 'red rum sir is murder'.replace(' ', '')])
print(ll, '->', is_palindrome_1(ll))
print(ll, '->', is_palindrome_2(ll))

ll.fill([ch for ch in 'hello world lol'.replace(' ', '')])
print(ll, '->', is_palindrome_1(ll))
print(ll, '->', is_palindrome_2(ll))

ll.fill([ch for ch in 'i did did i'.replace(' ', '')])
print(ll, '->', is_palindrome_1(ll))
print(ll, '->', is_palindrome_2(ll))

ll.fill([ch for ch in 'dd'.replace(' ', '')])
print(ll, '->', is_palindrome_1(ll))
print(ll, '->', is_palindrome_2(ll))
