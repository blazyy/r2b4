class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def enqueue(self, item):
        newNode = Node(item)
        if self.front == None: # queue is empty
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = self.rear.next

    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty!'
        return_num = self.front.data
        self.front = self.front.next
        return return_num

    def display(self):
        current = self.front
        print('F -> ', end = '')
        while current != None:
            print(current.data, end = ' ')
            current = current.next
        print('<- R', end = '')

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.enqueue(4)
q.enqueue(5)
q.display()
