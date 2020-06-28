from stack import Stack

def checkParentheses(str):
    stack = Stack()
    for char in str:
        if char == '(':
            stack.push(char)
        else:
            if not stack.isEmpty():
                stack.pop()
            else:
                return False
    if stack.isEmpty():
        return True
    return False

print(checkParentheses('((())(()))'))
print(checkParentheses('(()'))
