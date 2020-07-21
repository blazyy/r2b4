import random
import string


class Node:
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def is_left_child(self):
        if self.parent is not None and self == self.parent.left:
            return True
        return False

    def is_right_child(self):
        if self.parent is not None and self == self.parent.right:
            return True
        return False

    def has_no_children(self):
        if self.right is None and self.left is None:
            return True
        return False

    def has_one_child(self):
        if self.right is None and self.left is not None:
            return True
        elif self.right is not None and self.left is None:
            return True
        return False


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        '''I wanted to make this function recursive but couldn't since this
         is a magic function which means I can't add extra parameters'''
        # If tree is empty
        if self.root is None:
            self.root = Node(key, value)
        else:
            current = self.root
            while current:
                if key == current.key:
                    current.value = value
                    return
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, value, parent=current)
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, value, parent=current)
                        return
                    else:
                        current = current.right

    def __getitem__(self, key):
        current = self.root
        while current:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        raise KeyError(key)

    def __contains__(self, key):
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

    def find_min(self, node):
        while node.left:
            node = node.left
        return node.key

    def find_successor(self, node):
        # If right subtree of node is not null, succ is the smallest element
        # in the right subtree
        if node.right is not None:
            return self.find_min(self.right)
        else:
            # If node has no right child and is the left child of its parent,
            # then the parent is the successor.
            if node.is_left_child():
                return node.parent
            # If node has no right child and is is the right child of its parent
            # then the successor to this node is the successor of its parent
            # excluding this node.
            elif node.is_right_child():
                self.parent.right = None  # Temporarily excluding the node
                return self.find_successor(node.parent)
                self.parent.right = self
        return None

    def delete(self, key):
        # If node to delete is root and there's only one node in the tree
        if key == self.root.key and self.has_no_children(self.root):
            self.root = None
        else:
            if self.__contains__(self.root, key):
                current = self.root
                while current:
                    if key == current.key:
                        # If node to delete has no children
                        if current.has_no_children():
                            if current.parent.left == current:
                                current.parent.left = None
                            else:
                                current.parent.right = None
                        # If node to delete has one child
                        elif current.has_one_child():
                            # If node to delete has a left child
                            if current.left is not None:
                                current.left.parent = current.parent
                                if current.is_left_child():
                                    current.parent.left = current.left
                                else:
                                    current.parent.right = current.left
                            # If node to delete has a right child
                            elif current.right is not None:
                                current.right.parent = current.parent
                                if current.is_left_child():
                                    current.parent.left = current.right
                                else:
                                    current.parent.right = current.right
                            # If the node with one child is the root
                            elif current.parent is None:
                                if current.left is not None:
                                    self.root = current.left
                                    self.root.parent = None
                                else:
                                    self.root = current.right
                                    self.root.parent = None
                        # If node to delete has two children
                        else:
                            succ = self.find_succ(current)
                            current.key = succ.key
                            current.value = succ.value
                            # A succ is guaranteed to have 0-1 children.
                            # We could call delete() recursively, but that
                            # would start from the root and would take extra
                            # time, so we write deletion code again here.

                            # If succ has no children
                            if succ.has_no_children():
                                if succ.is_right_child():
                                    succ.parent.right = None
                                else:
                                    succ.parent.left = None
                            # If succ has one child
                            else:
                                if succ.left is not None:
                                    succ.left.parent = succ.parent
                                    if succ.is_left_child():
                                        succ.parent.left = succ.left
                                    else:
                                        succ.parent.right = succ.left
                                else:
                                    succ.right.parent = succ.parent
                                    if succ.is_left_child():
                                        succ.parent.left = succ.right
                                    else:
                                        succ.parent.right = succ.right
                        self.size -= 1
                        return
                    elif key < current.key:
                        current = current.left
                    else:
                        current = current.right
            else:
                raise KeyError(key)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.key, end=' ')
    inorder(node.right)


bst = BinarySearchTree()
size = 10
keys = [random.randint(1, 99) for i in range(size)]
values = [''.join([random.choice(string.ascii_letters) for i in range(4)]) for i in range(size)]
for i in range(size):
    bst[keys[i]] = values[i]
print('Keys:\t\t', ' '.join([str(key) for key in keys]))
print('Inorder:\t ', end='')
inorder(bst.root)
