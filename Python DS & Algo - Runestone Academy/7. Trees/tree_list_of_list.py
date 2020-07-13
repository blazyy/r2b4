def BinaryTree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    current_left = root[1]
    new_branch = BinaryTree(new_branch)
    new_branch[1] = current_left
    root[1] = new_branch


def insert_right(root, new_branch):
    current_right = root[2]
    new_branch = BinaryTree(new_branch)
    new_branch[2] = current_right
    root[2] = new_branch


def get_root(root):
    return root[0]


def set_root(root, root_val):
    root[0] = root_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


r = BinaryTree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
le = get_left_child(r)
print(le)
set_root(le, 9)
print(r)
insert_left(le, 11)
print(r)
print(get_right_child(get_right_child(r)))


'''
[5, [4, [], []], []]
[3, [9, [4, [], []], []], [7, [], [6, [], []]]]
[3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
[6, [], []]
'''
