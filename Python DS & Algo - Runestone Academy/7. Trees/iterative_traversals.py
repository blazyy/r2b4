from binary_tree import BinaryTree

def inorder_iterative(tree):
    stack = []
    current = tree
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.root, end='  ')
            current = current.right
        else:
            break


def preorder_iterative(tree):
    stack = []
    current = tree
    while True:
        if current:
            stack.append(current)
            print(current.root, end='  ')
            current = current.left
        elif stack:
            current = stack.pop()
            current = current.right
        else:
            break


def postorder_iterative(tree):
    

tree = BinaryTree()
tree.root = 1
tree.insert_left(2)
tree.left.insert_left(3)
tree.left.insert_right(4)
tree.insert_right(5)
tree.right.insert_left(6)
tree.right.insert_right(7)

tree.inorder()
print()
inorder_iterative(tree)

print()
print()

tree.preorder()
print()
preorder_iterative(tree)

# print()
# print()
#
# tree.postorder()
# print()
# postorder_iterative(tree)
