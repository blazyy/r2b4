from binary_tree import BinaryTree
from stack import Stack
import operator


def build_parse_tree(expr):
    expr = expr.split(' ')
    tree = BinaryTree('')
    stack = Stack()  # keeps track of parents nodes so we can return to them
    stack.push(tree)  # this is needed when the expr doesn't start with a '('

    for token in expr:
        if token == '(':
            tree.insert_left('')
            stack.push(tree)
            tree = tree.get_left()
        elif token in '+-/*':
            tree.set_root(token)
            tree.insert_right('')
            stack.push(tree)
            tree = tree.get_right()
        elif token == ')':
            tree = stack.pop()
        else:
            try:
                tree.set_root(int(token))
                tree = stack.pop()
            except ValueError:
                raise ValueError('{} is not a valid integer'.format(token))
    return tree


def eval_parse_tree(parse_tree):
    opers = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

    left_child = parse_tree.get_left()
    right_child = parse_tree.get_right()

    if left_child and right_child:
        fn = opers[parse_tree.get_root()]
        return fn(eval_parse_tree(left_child), eval_parse_tree(right_child))
    else:
        return parse_tree.get_root()


print(eval_parse_tree(build_parse_tree('( 3 + ( 4 * 5 ) )')))
