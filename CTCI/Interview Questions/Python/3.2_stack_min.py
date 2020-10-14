class Node:
    def __init__(self, data):
        self.data = data
        self.next_min = None

class Stack:
    def __init__(self):
        self.items = []
        self.min = None

    def push(self, item):
        if len(self.items) == 0:
            self.min = item
        else:
            if item < self.min:
                self.min = item
        self.items.append(item)

    def pop(self):
