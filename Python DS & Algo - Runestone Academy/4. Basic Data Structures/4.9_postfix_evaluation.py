from stack import Stack

def postfix_eval(expr):
    stack = Stack()
    for token in expr:
        if token in '0123456789':
            stack.push(int(token))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if token == '*':
                stack.push(op1 * op2)
            elif token == '/':
                stack.push(op2 / op1)
            elif token == '+':
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
    return stack.pop()

print(postfix_eval('78+32+/'))
# 3.0
