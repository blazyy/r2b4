# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.
# Page 67

import random

# Solution
# Using two stacks. One, for storing elements and the other to store the minimums. Only add to the minimum stack when the initial stack is empty or the new item that is being added is smaller than the current minimum (which is at the top of the minimum stack)
# Time Complexity: O(1) for all operations
# Space Complexity: O(n) (This only happens if you fill the stack with elements in descending order)
class Stack:
    def __init__(self):
        self.items = []
        self.mins = [] # This contains only the new minimums, i.e. numbers that are smaller than the current minimum.

    def push(self, item):
        if len(self.items) == 0 or item < self.mins[-1]:
            self.mins.append(item)
        self.items.append(item)

    def pop_back(self):
        if len(self.items) == 0:
            raise Exception("Cannot pop from empty list.")
        if self.items[-1] == self.mins[-1]:
            self.mins.pop()
        return self.items.pop()

    def get_min(self):
        return self.mins[-1]

stack = Stack()
elements = [random.randint(1, 100) for i in range(15)]
print(elements)

for element in elements:
    stack.push(element)

for i in range(15):
    print(stack.get_min(), end='  ')
    stack.pop_back()
