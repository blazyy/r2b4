# Implement a function to check if a binary tree is a binary search tree.

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, is_bst):
        self.root = Node(20)
        self.root.left = Node(10)
        self.root.right = Node(30)
        if is_bst:
            self.root.left.right = Node(15)
        else:
            self.root.left.right = Node(25)

# Solution 1
# Uses the fact that when traversing a valid BST inorder, the values will be in sorted order (ascending)
# Works for most cases but if there's a misplaced node that is more than one level apart, this algorith fails to detect it. Eg:
#               20
#             /   \
#           10     30
#            \
#             25
# This function returns true for this tree, which it shouldn't.
# Time Complexity: O(n)
# Space Complexity:  O(log N) or O(h) since we may recurse up to the depth of the tree
def validate_bst_1(node, prev=None):
    if node is None:
        return True
    if not validate_bst_1(node.left, prev):
        return False
    if prev is not None and node.val <= prev.val:
        return False
    prev = node
    if not validate_bst_1(node.right, prev):
        return False
    return True

# Solution 2
# Keeping track of min and max and each subtree and checking if the current node violates the BST property.
# Time Complexity: O(n)
# Space Complexity:  O(log N) or O(h) since we may recurse up to the depth of the tree
def validate_bst_2(root):
    return check_bst(root, None, None)

def check_bst(root, minimum, maximum):
    if root is None: # leaf node
        return True
    elif (minimum is not None and root.val <= minimum) or (maximum is not None and root.val >= maximum):
        return False
    else:
        return check_bst(root.left, minimum, root.val) and check_bst(root.right, root.val, maximum)

bt = BinaryTree(is_bst=True)
ibt = BinaryTree(is_bst=False)
print(validate_bst_1(bt.root))
print(validate_bst_2(bt.root))
print(validate_bst_1(ibt.root)) # Returns true, when answer should be false. Solution 1 isn't a complete solution.
print(validate_bst_2(ibt.root))
