class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__(self):
        self.head = None
        self.top = None

    def push(self, item):
        if self.head == None:
            self.head = self.top = self.prev = Node(item)
        else:
            self.top.next = Node(item)
            self.top.next.prev = self.top
            self.top = self.top.next

    def pop(self):
        return_ele = self.top.data
        self.top = self.top.prev
        self.top.next = None
        return return_ele

    def __str__(self):
        lst = []
        current = self.top
        while current:
            lst.append(current.data)
            current = current.prev
        return 'Top -> ' + ' '.join([str(item) for item in lst]) + ' <- Bottom'

s = Stack()
