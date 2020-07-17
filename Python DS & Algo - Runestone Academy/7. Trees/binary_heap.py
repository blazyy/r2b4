import random


class BinaryHeap:
    def __init__(self):
        self.heap = [0]  # 0 to make integer divison possible
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        idx = self.size  # no -1 since the first ele of heap list isn't used.
        while self.heap[idx] < self.heap[idx//2] and idx > 0:
            self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
            idx = idx // 2

    def del_min(self):
        return_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        idx = 1
        while idx * 2 <= self.size:
            # Finding min child
            l_idx = idx * 2
            r_idx = idx * 2 + 1
            if r_idx > self.size:
                min_child_idx = idx * 2
            else:
                if self.heap[l_idx] < self.heap[r_idx]:
                    min_child_idx = l_idx
                else:
                    min_child_idx = r_idx
            # Swapping current root with smaller child
            if self.heap[idx] > self.heap[min_child_idx]:
                self.heap[idx], self.heap[min_child_idx] = self.heap[min_child_idx], self.heap[idx]
                idx = min_child_idx
            else:
                break
        return return_val

    def __str__(self):
        return ' '.join(str(num) for num in self.heap)


bh = BinaryHeap()
lst_size = 10
lst = [random.randint(1, 100) for i in range(lst_size)]
print('Random List:\t\t\t', lst)
for num in lst:
    bh.insert(num)
print('Sorted List:\t\t\t', sorted(lst))
print('Binary Heap Deleted Minimums:\t', [bh.del_min() for i in range(lst_size)])
