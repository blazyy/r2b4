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
        self.end = None

    def is_empty(self):
        return self.head is None

    def append_using_pointer(self, item):
        if self.is_empty():
            self.head = Node(item)
            self.end = self.head
        else:
            self.end.set_next(Node(item))
            self.end = self.end.get_next()

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            temp = self.head
            while temp.get_next() is not None:
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

    def pop(self, index_to_pop=-1):
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
        idx = 0
        current = self.head
        prev = self.head
        if index_to_insert == 0:
            newNode = Node(item)
            newNode.set_next(self.head)
            self.head = newNode
        else:
            while current:
                if idx == index_to_insert:
                    newNode = Node(item)
                    prev.set_next(newNode)
                    newNode.set_next(current)
                prev = current
                current = current.get_next()
                idx += 1

    def remove(self, ele):
        current = prev = self.head
        # if element to remove is head
        if current.get_data() == ele:
            self.head = current.get_next()
        else:
            while current is not None:
                if current.get_data() == ele:
                    prev.set_next(current.get_next())
                    break
                prev = current
                current = current.get_next()
        self.size -= 1

    def search(self, ele):
        current = self.head
        idx = 0
        while current is not None:
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
        while current is not None:
            lst.append(current.get_data())
            current = current.get_next()
        return '[' + ', '.join(str(val) for val in lst) + ']'
