class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data = data
    def set_next(self, next):
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def is_empty(self):
        return self.head == None
    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            temp = self.head
            while temp.get_next() != None:
                temp = temp.get_next()
            temp.set_next(Node(item))
        self.size += 1
    def index(self, ele):
        idx = 0
        current = self.head
        while current:
            if current.get_data() == ele:
                return idx
            current = current.get_next()
            idx += 1
        return -1
    def pop(self, index_to_pop = -1):
        current = self.head
        if index_to_pop == -1:
            while current.get_next().get_next():
                current = current.get_next()
            return_num = current.get_next().get_data()
            current.set_next(None)
        elif index_to_pop == 0:
            return_num = current.get_data()
            self.head = current.get_next()
        else:
            previous = self.head
            idx = 0
            while current:
                if idx == index_to_pop:
                    return_num = current.get_data()
                    previous.set_next(current.get_next())
                idx += 1
                previous = current
                current = current.get_next()
        self.size -= 1
        return return_num
    def insert(self, item, index_to_insert):
        if index_to_insert > self.size:
            print('Index given is greater than size of list. Changing index to', self.size, 'which is the index of the list.')
            index_to_insert = self.size
        idx = 0
        current = self.head
        previous = self.head
        if index_to_insert == 0:
            newNode = Node(item)
            newNode.set_next(self.head)
            self.head = newNode
        elif index_to_insert == self.size:
            while current.get_next():
                current = current.get_next()
            current.set_next(Node(item))
        else:
            while current:
                if idx ==  index_to_insert:
                    newNode = Node(item)
                    prev.set_next(newNode)
                    newNode.set_next(current)
                prev = current
                current = current.get_next()
                idx += 1
        self.size += 1
    def remove(self, ele):
        current = prev = self.head
        # if element to remove is head
        if current.get_data() == ele:
            self.head = current.get_next()
        else:
            while current != None:
                if current.get_data() == ele:
                    prev.set_next(current.get_next())
                    break
                prev = current
                current = current.get_next()
        self.size -= 1
    def search(self, ele):
        current = self.head
        idx = 0
        while current != None:
            if current.get_data() == ele:
                return 'True: {}'.format(idx)
            idx += 1
            current = current.get_next()
        return False
    def slice(self, start_idx, end_idx):
        lst = []
        current = self.head
        idx = 0
        while current:
            if idx >= start_idx and idx < end_idx:
                lst.append(current.get_data())
            if idx >= end_idx:
                break
            current = current.get_next()
            idx += 1
        return '[' + ', '.join(str(val) for val in lst) + ']'
    def get_size(self):
        return self.size
    def get_index(self, ele):
        current = self.head
        idx = 0
        while current:
            if current.get_data() == ele:
                return idx
            idx += 1
            current = current.get_next()
        return -1
    def __str__(self):
        current = self.head
        lst = []
        while current != None:
            lst.append(current.get_data())
            current = current.get_next()
        return '[' + ', '.join(str(val) for val in lst) + ']'

class OrderedList(LinkedList):
    def append(self, item):
        '''Cannot append to an ordered list. Append here puts the value in its appropriate place.'''
        if self.head == None: # If list is empty
            self.head = Node(item)
        else:
            current = self.head
            if item <= current.data: # If element to insert is smallest in the list
                newNode = Node(item)
                newNode.set_next(self.head)
                self.head = newNode
            else: # If element goes anywhere other than the 0th index
                prev = self.head
                while current and current.data < item:
                    prev = current
                    current = current.get_next()
                newNode = Node(item)
                prev.set_next(newNode)
                newNode.set_next(current)
    def insert(self, item, index_to_insert):
        print('Cannot insert to an index in an ordered list!')

ll = LinkedList()
ol = OrderedList()
ll.append(56)
ll.append(11)
ll.append(244)
ll.append(7)
ll.append(99)
ll.insert(18, 0)
ll.insert(37, 1)
ll.insert(999, 7)
ol.insert(66, 7)
