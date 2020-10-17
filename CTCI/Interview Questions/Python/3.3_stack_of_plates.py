# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to  a single stack (that is, pop() should return the same values as it would if there were just a single stack.)

# FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack.

import random

class SetOfStacks:
    def __init__(self, threshold=5):
        self.threshold = threshold
        self.stacks = []
        self.stacks.append([])
        self.current_stack = 0

    def push(self, item):
        if len(self.stacks[self.current_stack]) == self.threshold:
            self.stacks.append([])
            self.current_stack += 1
        self.stacks[self.current_stack].append(item)

    def pop(self):
        if self.current_stack == 0 and len(self.stacks[self.current_stack]) == 0:
            print('Cannot pop from empty list!')
        if len(self.stacks[self.current_stack]) == 0:
            self.stacks.pop()
            self.current_stack -= 1

        return self.stacks[self.current_stack].pop()

    def __str__(self):
        return str(self.stacks)

stack = SetOfStacks()

lst = [random.randint(1, 100) for i in range(27)]
for num in lst:
    stack.push(num)
print(stack)

for i in range(10):
    print(stack.pop())
