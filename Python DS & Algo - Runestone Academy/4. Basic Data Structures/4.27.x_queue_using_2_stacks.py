from stack import Stack

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        if self.outbox.isEmpty():
            while not self.inbox.isEmpty():
                self.outbox.push(self.inbox.pop())
        return self.outbox.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
