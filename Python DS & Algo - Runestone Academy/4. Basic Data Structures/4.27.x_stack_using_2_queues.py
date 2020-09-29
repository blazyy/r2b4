from queue import Queue


class Stack:
    def __init__(self):
        self.queueA = Queue()
        self.queueB = Queue()

    def push(self, item):
        if self.queueA.isEmpty():
            self.queueA.enqueue(item)
            while not self.queueB.isEmpty():
                self.queueA.enqueue(self.queueB.dequeue())
        else:
            self.queueB.enqueue(item)
            while not self.queueA.isEmpty():
                self.queueB.enqueue(self.queueA.dequeue())

    def pop(self):
        if self.queueA.isEmpty():
            return self.queueB.dequeue()
        return self.queueA.dequeue()
