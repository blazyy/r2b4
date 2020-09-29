from stack import Stack
from binary_tree import BinaryTree
import operator

def build_parse_tree(expr):
    tree = BinaryTree()
    parent_stack = Stack()
    parent_stack.push(tree) # this is needed when the expr doesn't start with a '('
    for token in expr.split(' '):
        if token == '(':
            tree.insert_left(' ')
            parent_stack.push(tree)
            tree = tree.left
        elif token in '0123456789':
            tree.root = token
            tree = parent_stack.pop()
        elif token in '^*/+-':
            tree.root = token
            parent_stack.push(tree)
            tree.insert_right(' ')
            tree = tree.right
        else:
            tree = parent_stack.pop()
    return tree

def eval_parse_tree(parse_tree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    left_child = parse_tree.left
    right_child = parse_tree.right

    if left_child and right_child:
        fn = opers[parse_tree.root]
        return fn(int(eval_parse_tree(left_child)), int(eval_parse_tree(right_child)))
    else:
        return parse_tree.root

print(eval_parse_tree(build_parse_tree('( 3 + ( 4 * 5 ) )')))
