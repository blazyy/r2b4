class BinaryTree:
    def __init__(self):
        self.root = None
        self.left = None
        self.right = None

    def insert_left(self, value):
        new_node = BinaryTree()
        new_node.set_root(value)
        if self.left is None:
            self.left = new_node
        else:
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        new_node = BinaryTree()
        new_node.set_root(value)
        if self.right is None:
            self.right = new_node
        else:
            new_node.right = self.right
            self.right = new_node

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_root(self):
        return self.root

    def set_root(self, new_root):
        self.root = new_root


def preorder(tree):
    if tree is not None:
        print(tree.get_root(), ' ', end='')
        preorder(tree.get_left())
        preorder(tree.get_right())


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left())
        print(tree.get_root(), ' ', end='')
        inorder(tree.get_right())


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_root(), ' ', end='')


tree = BinaryTree()
tree.set_root(1)
tree.insert_left(2)
tree.get_left().insert_left(3)
tree.get_left().insert_right(4)
tree.insert_right(5)
tree.get_right().insert_left(6)
tree.get_right().insert_right(7)
preorder(tree)
print()
inorder(tree)
print()
postorder(tree)
