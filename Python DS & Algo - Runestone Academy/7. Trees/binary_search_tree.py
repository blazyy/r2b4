class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def get_left(self):
        return self.left

    def set_left(self, new_left):
        self.left = new_left

    def set_right(self, new_right):
        self.right = new_right

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.get_root().__iter__()

    def get_root(self):
        return self.root

    def set_root(self, new_root):
        self.root = new_root

    def put(self, key, value):
        if self.get_root() is None:
            self.set_root(Node(key, value))
        else:
            current = self.get_root()
            while current:
                # If new key is lower than current key, go left
                if key < current.get_key():
                    if current.get_left() is None:
                        current.left = Node(key, value, parent=current)
                        self.size += 1
                        break
                    else:
                        current = current.get_left()
                # If new key is greater than current key, go right
                elif key > current.get_key():
                    if current.get_right() is None:
                        current.right = Node(key, value, parent=current)
                        self.size += 1
                        break
                    else:
                        current = current.get_right()
                # If new key already exists in tree, overwrite existing value
                else:
                    current.value = value
                    break

    def __setitem__(self, key, value):
        self.put(self, key, value)

    def get(self, key):
        if self.get_root() is None:
            return None
        else:
            current = self.get_root()
            while current:
                if key == current.get_key():
                    return current.value
                elif key < current.get_key():
                    current = current.get_left()
                else:
                    current = current.get_right()
            raise KeyError('Key does not exist!')

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return True if self.get(key) else False

    def find_min(self, current_node):
        '''
        Returns the smallest key in the tree.
        This will be the leftmost child of the tree.
        '''
        current = current_node
        while current.get_left():
            current = current.get_left()
        return current

    def get_successor(self, current):
        successor = None
        if current.get_right() is not None:
            successor = self.find_min(current)
        else:
            if current == current.get_parent().get_left():
                successor = current.get_parent()
            if current == current.get_parent().get_right():
                current.get_parent().set_right(None)
                successor = self.get_successor(current.get_parent())
                current.get_parent().set_right(current)

        return successor

    def delete(self, key):
        # If tree has only one node which needs to be deleted
        if self.size == 1 and self.get_root().get_key() == key:
            self.set_root(None)
        else:
            current = self.get_root()
            while current:
                if key == current.get_key():
                    # If node to delete has no children
                    if current.get_left() is None and current.get_right() is None:
                        # To check if node to delete is left or right child
                        parent = current.get_parent()
                        if parent.get_left() == current:
                            parent.set_left(None)
                        else:
                            parent.set_right(None)
                    # If node to delete has one child
                    elif (current.get_left() is None and current.get_right() is not None) or (current.get_left() is not None and current.get_right() is None):
                        # If node with one child is the root
                        if current.get_parent() is None:
                            if current.get_left() is not None:
                                current.get_left().set_parent(None)  # New root will have no parent
                                self.set_root(current.get_left())
                            else:
                                current.get_right().set_parent(None)
                                self.set_root(current.get_right())
                        else:
                            if current.get_left() is not None:
                                current.get_left().set_parent(current.get_parent())
                                current = current.get_left()
                            else:
                                current.get_right().set_parent(current.get_parent())
                                current = current.get_right()
                    # If node to delete has two children
                    else:
                        # Find successor, i.e. node to replace the node to be deleted
                        '''
                         A successor is a node that will preserve the binary search tree
                         property for both of the existing left and right subtrees.
                         The node that will do this is the node that has the next-largest
                         key in the tree
                        '''
                        successor = current.get_successor()
                    return
                elif key < current.get_key():
                    current = current.get_left()
                else:
                    current = current.get_right()
            raise KeyError('Key does not exist!')
