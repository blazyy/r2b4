# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of thr two subtrees of any node never differ by more than one.

INT_MIN = float('-inf') # Not exactly INT_MIN but let's just pretend

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, values):
        self.root = self.populate_tree(values, None, 0)

    def populate_tree(self, values, root, i):
        if i < len(values):
            root = Node(values[i])
            root.left = self.populate_tree(values, root.left, 2 * i + 1)
            root.right = self.populate_tree(values, root.right, 2 * i + 2)
        return root

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        if root.val is not None:
            print(root.val, end=' ')
        self.inorder(root.right)

    def get_height(self, root):
        if root is None or root.val is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    # Solution 1
    # Recurse through tree, and for each node, compute the heights of each subtree
    # Time Complexity: O(n log n), since each node is 'touched' once per node above it
    # Space Complexity: O(n) 
    def is_balanced_1(self, root):
        if root is None or root.val is None:
            return True
        if abs(self.get_height(root.left) - self.get_height(root.right)) > 1:
            return False
        else:
            return self.is_balanced_1(root.left) and self.is_balanced_1(root.right)

    def check_height(self, root):
        if root is None or root.val is None:
            return -1
        left_height = self.check_height(root.left)
        if left_height == INT_MIN:
            return INT_MIN
        right_height = self.check_height(root.right)
        if right_height == INT_MIN:
            return INT_MIN
        height_diff = abs(left_height - right_height)
        if height_diff > 1:
            return INT_MIN
        else:
            return max(left_height, right_height) + 1

    # Solution 2
    # In order to reduce the number of calls to get_height in solution 1, we check if the tree is balanced at the same time as it's checking heights. If unbalanced, return INT_MIN as an error code
    # Time Complexity: O(n)
    # Space Complexity: O(h)
    def is_balanced_2(self, root):
        return self.check_height(root) != INT_MIN


balanced_tree = BinaryTree([1, 2, 3, None, 5, None, 7])
print(balanced_tree.is_balanced_1(balanced_tree.root))
print(balanced_tree.is_balanced_2(balanced_tree.root))
# unbalanced_tree = BinaryTree([8, 3, 10, None, None, None, 15, None, None, None, None, None, None, 13, None])
unbalanced_tree = BinaryTree([8, 3, None, 1, None, None, None])
print(unbalanced_tree.is_balanced_1(unbalanced_tree.root))
print(unbalanced_tree.is_balanced_2(unbalanced_tree.root))
