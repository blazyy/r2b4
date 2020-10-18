# Implement a MyQueue class which implements a queue using two stacks.

# Solution
# Using a default Python list as our stack
# Remember that pushing items into and popping them out of a stack reverses their order. Do this again, and the order stays the same. This is what we want, since a queue operates on the FIFO basis.
# Time Complexity: O(1) for enqueue, O(n) for dequeue
# Space Complexity: O(n)? Due to extra stack?
class MyQueue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if len(self.outbox) == 0:
            if len(self.inbox) == 0:
                print('Cannot dequeue from empty queue!')
                return None
            while len(self.inbox) != 0:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()

queue = MyQueue()
queue.enqueue(1); queue.enqueue(2); queue.enqueue(3); queue.enqueue(4); queue.enqueue(5)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
