class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class OrderedList():
    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head == None: # If list is empty
            self.head = Node(item)
        else:
            current = self.head
            if item <= current.data: # If element to insert is smallest in the list
                newNode = Node(item)
                newNode.next = self.head
                self.head = newNode
            else: # If element goes anywhere other than the 0th index
                prev = self.head
                while current and current.data < item:
                    prev = current
                    current = current.next
                newNode = Node(item)
                prev.next = newNode
                newNode.next = current

    def remove(self, item):
        if self.head == None:
            return
        current = self.head
        if current.data == item: # If element to remove is the head
            self.head = current.next
        else:
            current = self.head.next
            prev = self.head
            while current:
                if current.data == item:
                    prev.next = current.next
                    return
                prev = current
                current = current.next

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def index(self, item):
        current = self.head
        idx = 0
        while current:
            if current.data == item:
                return idx
            current = current.next
            idx += 1
        return -1

    def pop(self, index_to_pop = -1):
        if index_to_pop == -1: # If element to pop is last in the list
            current = self.head
            while current.next.next:
                current = current.next
            return_item = current.next.data
            current.next = None
            return return_item
        else:
            current = self.head
            prev = self.head
            idx = 0
            return_num = -1
            while current:
                if idx == index_to_pop:
                    return_num = current.data
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                idx += 1
            return return_num

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        current = self.head
        lst = []
        while current:
            lst.append(current.data)
            current = current.next
        return '[' + ', '.join([str(ele) for ele in lst]) + ']'

ol = OrderedList()
