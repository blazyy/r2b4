# Write an algorithm to find the "next" node, i.e. the inorder successor of a given node in a BST. You may assume that each node has a link to its parent.

from binarytree import bst, get_parent

# Solution
# Using the following rules to find the successor:
# 1) If the node has a right child, then the successor is the smallest key in the right subtree.
# 2) If the node has no right child and is the left child of its parent, then the parent is the successor.
# 3) If the node has no right child and is the right child of its parent, then the successor to this node is the successor of its parent, excluding this node.
def find_succesor(root, node):
    if node is None:
        return None
    succ = None
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        succ = current
    else:
        parent = get_parent(root, node)
        if parent:
            if parent.left == node: # If node is the left child of its parent
                succ = parent
            elif parent.right == node:
                parent.right = None # Setting current node to be None. Read rules above.
                succ = find_succesor(root, parent)
                parent.right = node # Setting it back
    return succ

my_tree = bst(height=4)
print(my_tree)
node = my_tree
successor = find_succesor(my_tree, node)
print('node: \t\t{}\nsuccessor: \t{}'.format(node.val, successor.val))
