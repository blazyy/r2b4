class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.end = None

    def is_empty(self):
        return self.size == 0

    def append(self, item):
        if self.head is None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(item)
        self.size += 1

    def index(self, ele):
        idx = 0
        current = self.head
        while current:
            if current.data == ele:
                return idx
            current = current.next
            idx += 1
        return -1

    def pop(self, index_to_pop=-1):
        if self.head is None:
            raise Exception('Cannot pop, list is empty!')
        if index_to_pop > self.size - 1:
            raise IndexError('That index does not exist!')
        if index_to_pop == -1:
            index_to_pop = self.size - 1
        if index_to_pop == 0:
            return_ele = self.head.data
            self.head = self.head.next
        else:
            idx = 0
            current = self.head
            prev = current
            while current:
                if idx == index_to_pop:
                    return_ele = current.data
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                idx += 1
        self.size -= 1
        return return_ele

    def insert(self, item, index_to_insert):
        if index_to_insert > self.size - 1:
            raise IndexError('Index cannot be greater than size!')
        new_node = Node(item)
        if index_to_insert == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = current
            idx = 0
            while current:
                if idx == index_to_insert:
                    new_node.next = current
                    prev.next = new_node
                    break
                prev = current
                current = current.next
                idx += 1
        self.size += 1

    def remove(self, ele):
        if self.head is None:
            raise Exception('Cannot remove, list is empty!')
        if self.head.data == ele:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            current = self.head
            prev = current
            while current:
                if current.data == ele:
                    prev.next = current.next
                    self.size -= 1
                    return
                prev = current
                current = current.next
            raise Exception('Element not found!')


    def search(self, ele):
        if self.head is None:
            raise Exception('Cannot search if the list is empty!')
        if self.head.data == ele:
            return True
        current = self.head.next
        while current:
            if current.data == ele:
                return True
            current = current.next
        return False

    def slice(self, start_idx, end_idx):
        if start_idx < 0 or end_idx > self.size - 1:
            raise IndexError('Invalid indexes!')
        current = self.head
        idx = 0
        sliced = []
        while current:
            if idx == start_idx:
                sliced = []
                if start_idx == end_idx:
                    return sliced
                while idx != end_idx:
                    sliced.append(current.data)
                    current = current.next
                    idx += 1
                return sliced
            current = current.next
            idx += 1

    def get_size(self):
        return self.size

    def get_index(self, ele):
        if self.head.data == ele:
            return 0
        current = self.head.next
        idx = 1
        while current:
            if current.data == ele:
                return idx
            current = current.next
            idx += 1

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return ' '.join([str(element) for element in elements])
