from stack import Stack

def balanced_parentheses(expr):
    stack = Stack()
    return_code = ''
    for token in expr:
        if token.isalpha():
            return_code = 'alpha' # expression contains alphabets
            break
        if token == '(':
            stack.push(token)
        elif token == ')':
            if stack.isEmpty() or stack.pop() != '(':
                return_code = 'ubp' # ubp = unbalanced parentheses
                break
            else:
                continue
    if stack.isEmpty() and return_code == '': # The second condition is so that the return_code doesn't get overwritten to 'bp' in case the first tokenacter of the expression is an alphabet
        return_code = 'bp' # bp = balanced parentheses
    return return_code

def infix_to_postfix(infix_expr):
    infix_expr = infix_expr.split(' ')
    return_code = balanced_parentheses(infix_expr)
    if return_code == 'bp':
        result = []
        stack = Stack()
        precedence = {'^' : 4, '*' : 3, '/' : 3, '+' : 2, '-' : 2, '(' : 1}
        for token in infix_expr:
            if token.isalnum():
                result.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                top = stack.pop()
                while not stack.isEmpty() and top != '(':
                    result.append(top)
                    top = stack.pop()
            else:
                while not stack.isEmpty() and precedence[stack.peek()] >= precedence[token]:
                    result.append(stack.pop())
                stack.push(token)
        while not stack.isEmpty():
            result.append(stack.pop())
        return ' '.join(result)
    elif return_code == 'ubp':
        return 'Parentheses not balanced!'
    else:
        return 'No alphabets allowed in expression!'

def postfix_eval(postfix_expr):
    if postfix_expr == 'No alphabets allowed in expression!' or postfix_expr == 'Parentheses not balanced!':
        return ''
    stack = Stack()
    postfix_expr = postfix_expr.split(' ')
    for token in postfix_expr:
        if token.isnumeric():
            stack.push(int(token))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if token == '+':
                stack.push(op1 + op2)
            elif token == '-':
                stack.push(op1 - op2)
            elif token == '/':
                stack.push(op2 / op1)
            else:
                stack.push(op1 * op2)
    return stack.pop()

print(infix_to_postfix('A + B * ( C / D ) + F * ( G + H )')) # ABCD/*FGH+*++
print(infix_to_postfix('12 + 24 * ( 360 / 49 ) + 53 * ( 26 + 37 )'))
print(postfix_eval(infix_to_postfix('12 + 24 * ( 360 / 49 ) + 53 * ( 26 + 37 )')))
