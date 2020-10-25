# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
# Page 75

import random

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, values):
        self.root = None
        self.construct_bst(values, 0, len(values) - 1)

    # Solution
    # Kinda like binary search. Pretty simple solution.
    # Time Complexity: O(n)
    def construct_bst(self, values, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(values[mid])
        if self.root is None:
            self.root = node
        node.left = self.construct_bst(values, start, mid - 1)
        node.right = self.construct_bst(values, mid + 1, end)
        return node

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val, end=' ')
        self.inorder(node.right)

def gen_array(n, upper_bound=100):
    """Generates and returns an array that is sorted without any duplicates."""
    if n >= upper_bound:
        raise Exception('Upper bound is too high! Either increase it or increase the number of elements in the array')
    arr = []
    while len(arr) <= n:
        rand_num = random.randint(1, upper_bound)
        if rand_num not in arr:
            arr.append(rand_num)
    return sorted(arr)

arr = gen_array(10)
bst = BinarySearchTree(arr)
bst.inorder(bst.root)
