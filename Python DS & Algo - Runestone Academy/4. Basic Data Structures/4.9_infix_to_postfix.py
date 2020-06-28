from stack import Stack

def infix_to_postfix(expr):
    stack = Stack()
    postfix = ''
    precedence = {'*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1}
    for token in expr:
        if token.isalpha():
            postfix += token
        elif token == '(':
            stack.push(token)
        # Since the parentheses govern precedence, we have to make sure the
        # operations inside them are done first. This is why the operators are
        # popped immediately when a closing bracket is seen.
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(' and not stack.isEmpty():
                postfix += top_token
                top_token = stack.pop()
        else:
            while not stack.isEmpty() and precedence[stack.peek()] >= precedence[token]:
                postfix += stack.pop()
            stack.push(token)
    while not stack.isEmpty():
        postfix += stack.pop()
    return postfix
print(infix_to_postfix("A*B+C*D"))
# A B * C D * +

print(infix_to_postfix("(A+B)*C-(D-E)*(F+G)"))
# A B + C * D E - F G + * -

print(infix_to_postfix('A+B*(C/D)+F*(G+H)')) # ABCD/*FGH+*++
