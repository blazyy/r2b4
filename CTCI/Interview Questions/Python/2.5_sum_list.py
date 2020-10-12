# You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a funciton that adds the two numbers and returns the sum as a linked list.
# Input  (7 -> 1 -> 6) + (5 -> 9 -> 2) (That is, 617 + 295)
# Output 2 -> 1 -> 9 (That is, 912)

# Suppose the digits are stored in forward order. Repeat the above problem.
# Input  (6 -> 1 -> 7) + (2 -> 9 -> 5) (That is, 617 + 295)
# Output 9 -> 1 -> 2 (That is, 912)

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

def create_linked_lists(reverse=False):
    list_a = LinkedList()
    list_b = LinkedList()
    # num1 = random.randint(100, 999)
    num1 = 98654
    num2 = 179
    # num2 = random.randint(100, 999)
    num1_to_return = num1
    num2_to_return = num2
    while num1:
        list_a.append(num1 % 10)
        num1 //= 10
    while num2:
        list_b.append(num2 % 10)
        num2 //= 10
    return num1_to_return, num2_to_return, list_a, list_b

# Solution
# Since addition can also be done in reverse, just traverse the linked list while keeping in mind that there's a possibility of a carry.
# Time Complexity: O(n + m), Space Complexity(O(n + m)) where n and m are the number of digits in each number that's being added.
def add_linked_lists_reverse(list_a, list_b):
    ll_sum = LinkedList()
    carry = 0
    list_a_current = list_a.head
    list_b_current = list_b.head
    while list_a_current or list_b_current:
        current_sum = 0
        if list_a_current:
            current_sum += list_a_current.data
            list_a_current = list_a_current.next
        if list_b_current:
            current_sum += list_b_current.data
            list_b_current = list_b_current.next
        current_sum += carry
        if current_sum >= 10:
            ll_sum.append(current_sum % 10)
            carry = 1
        else:
            ll_sum.append(current_sum)
            carry = 0
    if carry:
        ll_sum.append(carry)
    return ll_sum

# Solution B
# I tried implementing this on my own but I got way too annoyed while trying to so I'm skipping this for now and I will kick myself in the future when I get asked this in an interview.

num1, num2, list_a, list_b = create_linked_lists(reverse = True)
print('{} + {} = {}'.format(num1, num2, num1 + num2))
print(list_a)
print(list_b)
ll_sum = add_linked_lists_reverse(list_a, list_b)
print(ll_sum)
