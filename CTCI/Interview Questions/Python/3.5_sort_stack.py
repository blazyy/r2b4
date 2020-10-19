# Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may NOT copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
# Page 67

import random

# Solution
# The buffer stack will always be sorted when building it. Taking the current element (most recently popped from original stack), pop all elements greater than it from the buffer to the original stack (yes, the original stack), and then put the element into the buffer. My explanation is pretty bad lol so if the future me is confused just refer back to the book.
# Time Complexity: O(n^2)
# Space Complexity: Doesn't make sense to mention here but it's O(n)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def sort_stack(self):
        if self.is_empty():
            return
        buffer = []
        while len(self.items) > 0:
            current = self.items.pop()
            while len(buffer) > 0 and buffer[-1] > current:
                self.push(buffer.pop())
            buffer.append(current)
        while len(buffer) != 0:
            self.push(buffer.pop())

    def __str__(self):
        return ' '.join([str(ele) for ele in self.items])

stack = Stack()
lst = [stack.push(random.randint(1, 100)) for i in range(10)]
print(stack)
stack.sort_stack()
print(stack)
