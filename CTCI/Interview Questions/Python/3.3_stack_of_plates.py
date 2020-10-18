# Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to  a single stack (that is, pop() should return the same values as it would if there were just a single stack.)

# FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack.

import random

# Solution
# Nothing to explain here. Pretty simple but kinda long.
# Time Complexity: O(n) - for pop_at(), due to left_shift(). Other operations are 0(1)
# Space Complexity - Not relevant.
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

    def left_shift(self, stack, index):
        while stack <= self.current_stack:
            for i in range(index, len(self.stacks[stack]) - 1):
                self.stacks[stack][i] = self.stacks[stack][i + 1]
            if stack < self.current_stack: # This condition deals with shifting the first element of the next stack to the last element of the previous stack.
                self.stacks[stack][self.threshold - 1] = self.stacks[stack + 1][0]
            index = 0
            stack += 1
        self.pop() # Since we're left shifting, there is a duplicate element at the last, we just remove it using pop.

    def pop_at(self, stack, index):
        if stack > self.current_stack or stack < 0 or index >= self.threshold or index < 0:
            print("Invalid stack/element index!")
            return None
        if stack == self.current_stack:
            if index >= len(self.stacks[stack]):
                print("Invalid stack/element index!")
                return None
            elif index == len(self.stacks[self.current_stack]) - 1: # If index to pop is last element, use pop() function.
                return self.pop()
        popped = self.stacks[stack][index]
        self.left_shift(stack, index)
        return popped

    def __str__(self):
        return str(self.stacks)

random.seed(69)
stack = SetOfStacks()

lst = [random.randint(1, 100) for i in range(27)]
for num in lst:
    stack.push(num)
print(stack)

print("Popped {}".format(stack.pop_at(index=3, stack=3)))
print(stack)
