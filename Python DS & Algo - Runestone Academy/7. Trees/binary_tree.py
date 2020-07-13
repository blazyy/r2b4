class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if self.left is None:
            self.left = BinaryTree(new_node)
        else:
            new_node = BinaryTree(new_node)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, new_node):
        if self.right is None:
            self.right = BinaryTree(new_node)
        else:
            new_node = BinaryTree(new_node)
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
