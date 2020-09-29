class BinaryTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert_left(self, val):
        new_node = BinaryTree()
        new_node.root = val
        if self.left is None:
            self.left = new_node
        else:
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, val):
        new_node = BinaryTree()
        new_node.root = val
        if self.right is None:
            self.right = new_node
        else:
            new_node.right = self.right
            self.right = new_node


def preorder(tree):
    if tree is not None:
        print(tree.root, ' ', end='')
        preorder(tree.left)
        preorder(tree.right)


def inorder(tree):
    if tree is not None:
        inorder(tree.left)
        print(tree.root, ' ', end='')
        inorder(tree.right)


def postorder(tree):
    if tree is not None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.root, ' ', end='')



# tree = BinaryTree()
# tree.root = 1
# tree.insert_left(2)
# tree.left.insert_left(3)
# tree.left.insert_right(4)
# tree.insert_right(5)
# tree.right.insert_left(6)
# tree.right.insert_right(7)
# preorder(tree)
# print()
# inorder(tree)
# print()
# postorder(tree)
