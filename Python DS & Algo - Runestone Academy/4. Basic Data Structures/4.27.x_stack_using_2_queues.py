from queue import Queue

class Stack:
    def __init__(self):
        self.queue_a = Queue()
        self.queue_b = Queue()

    def push(self, item):
        if self.queue_a.isEmpty():
            self.queue_a.enqueue(item)
            while not self.queue_b.isEmpty():
                self.queue_a.enqueue(self.queue_b.dequeue())
        elif self.queue_b.isEmpty():
            self.queue_b.enqueue(item)
            while not self.queue_a.isEmpty():
                self.queue_b.enqueue(self.queue_a.dequeue())

    def pop(self):
        if self.queue_a.isEmpty():
            return self.queue_b.dequeue()
        return self.queue_a.dequeue()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
