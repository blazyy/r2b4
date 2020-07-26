from binary_search_tree import BinarySearchTree, Node


class AVLTree(BinarySearchTree):
    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def __setitem__(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            current = self.root
            while current:
                if key == current.key:
                    current.value = value
                elif key < current.key:
                    if current.left is None:
                        current.left = Node(key, value, parent=current)
                        self.update_balance(current.left)
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = Node(key, value, parent=current)
                        self.update_balance(current.right)
                        break
                    else:
                        current = current.right

    def rotate_left(self, rot_root):
        new_root = rot_root.right
        if new_root.left is not None:
            rot_root.right = new_root.left
            new_root.left.parent = rot_root
        new_root.parent = rot_root.parent
        # If rot_root is BST's root
        if rot_root.parent is None:
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right = new_root
        new_root.left = rot_root
        rot_root.parent = new_root

    def rotate_right(self, rot_root):
        new_root = rot_root.left
        if new_root.right is not None:
            rot_root.left = new_root.right
            new_root.right.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.parent is None:
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left = new_root
            else:
                rot_root.parent.right = new_root
        new_root.right = rot_root
        rot_root.parent = new_root
