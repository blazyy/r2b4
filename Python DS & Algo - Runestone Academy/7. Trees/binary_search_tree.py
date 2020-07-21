class Node:
    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        # If tree is empty
        if self.root is None:
            self.root = Node(key, value)
            self.size += 1
        else:
            current = self.root
            while current:
                if key == current.key:
                    current.value = value
                    return
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, value, parent=current)
                        self.size += 1
                        return
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, value, parent=current)
                        self.size += 1
                        return
                    else:
                        current = current.right

    def __getitem__(self, key):
        if self.root is None:
            raise KeyError(key)
        else:
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

    def delete(self, key):
        # If node to delete is root and there's only one node in the tree
        if self.size == 1 and key == self.root.key:
            self.root = None
        else:
            if self.__contains__(key):
                current = self.root
                while current:
                    if key == current.key:
                        # If node to delete has no children
                        if current.left is None and current.right is None:
                            if current.parent.left == current:
                                current.parent.left = None
                            else:
                                current.parent.right = None
                        # If node to delete has one child
                        elif (current.left is None and current.right is not None) or (current.left is not None and current.right is None):
                            if current.left is not None:
                                current.left.parent = current.parent
                                current.parent.left = current.left
                            else:
                                current.right.parent = current.parent
                                current.parent.right = current.right
                        # If node to delete has two children
                        else:
                            successor = current.find_successor()

                        self.size -= 1
                        return
                    elif key < current.key:
                        current = current.left
                    else:
                        current = current.right
            else:
                raise KeyError(key)

bst = BinarySearchTree()
bst[45] = 'yolo'
print(45 in bst)
print(66 in bst)
print(len(bst))
