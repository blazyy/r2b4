import random

class BinaryHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.perc_up(self.size)


    def perc_up(self, idx):
        while idx // 2 > 0:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = self.heap[idx//2], self.heap[idx]
            idx //= 2

    def del_min(self):
        return_val = self.heap[1]
        self.heap[1] = self.heap[self.size] # replacing root node with last node in heap
        self.heap.pop()
        self.size -= 1
        self.perc_down(1)
        return return_val

    def perc_down(self, idx):
        while idx * 2 <= self.size:
            min_child_idx = self.get_min_child_idx(idx)
            if self.heap[idx] > self.heap[min_child_idx]:
                self.heap[idx], self.heap[min_child_idx] = self.heap[min_child_idx], self.heap[idx]
            idx = min_child_idx

    def get_min_child_idx(self, idx):
        if (idx * 2 + 1) > self.size:
            # If there is no right child, return left child's index
            return idx * 2
        else:
            if self.heap[idx * 2] < self.heap[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1

    def build_heap(self, lst):
        self.size = len(lst)
        self.heap = [0] + lst[:]
        idx = len(lst) // 2
        while idx > 0:
            self.perc_down(idx)
            idx -= 1

    def __str__(self):
        return ' '.join(str(num) for num in self.heap)

size = 10
lst = [random.randint(1, 100) for i in range(size)]
bh = BinaryHeap()
bh.build_heap(lst)
print('Random List:\t\t\t', lst)
print('Sorted List:\t\t\t', sorted(lst))
print('Binary Heap Deleted Minimums:\t', [bh.del_min() for i in range(size)])
