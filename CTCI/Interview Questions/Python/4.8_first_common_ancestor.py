# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This not not necessarily a binary search tree.

from binarytree import tree, bst

# BST. Not a part of the question but just wanted to try it out.
def find_common_ancestor_bst(root, node1, node2):
    if node1.val < root.val and node2.val < root.val:
        return find_common_ancestor_bst(root.left, node1, node2)
    elif node1.val > root.val and node2.val > root.val:
        return find_common_ancestor_bst(root.right, node1, node2)
    else:
        return root

# my_bst = bst(height=5)
# print(my_bst)
# node1 = my_bst.left
# node2 = my_bst.right
# fca = find_common_ancestor_bst(my_bst, node1, node2)
# print('FCA of {} and {} is {}'.format(node1.val, node2.val, fca.val))

root = tree(height=4, is_perfect=True)
node1s = [root.left, root.left.left, root.left.left.right.right, root.left.left.left]
node2s = [root.right, root.right.right, root.right.right.right.left, root.left.left.right]
print(root)

# Solution
# Traverse the entire tree, in postorder fashion. How the algorithm works is for each subtree, it returns a value. It returns NULL if the node we're looking for isn't in the subtree, else, it returns the node itself. When we know that left and right subtrees contain a value that is NOT NULL, we know that we have found the two nodes we're looking for, and that the current node we're at is the first common ancestor.
def find_common_ancestor(root, node1, node2):
    if root is None:
        return None
    if root == node1 or root == node2:
        return root
    left = find_common_ancestor(root.left, node1, node2)
    right = find_common_ancestor(root.right, node1, node2)
    if left is None and right is None:
        return None
    if left is None:
        return right
    elif right is None:
        return left
    else: # if both are not null, this is our result
        return root

for node1, node2 in zip(node1s, node2s):
    fca = find_common_ancestor(root, node1, node2)
    print('FCA of {} and {} is {}'.format(node1.val, node2.val, fca.val))
