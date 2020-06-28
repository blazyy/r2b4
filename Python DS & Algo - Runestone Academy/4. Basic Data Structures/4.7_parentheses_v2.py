from stack import Stack

def checkParentheses(str):
    stack = Stack()
    for char in str:
        if char in '([{':
            stack.push(char)
        else:
            if stack.isEmpty():
                return False
            if '([{'.index(stack.pop()) != ')]}'.index(char):
                return False
    if stack.isEmpty():
        return True
    return False
#print(checkParentheses('{({([][])}())}'))
#print(checkParentheses('[{()]'))

print(checkParentheses('{{([][])}()}'))
print(checkParentheses('[[{{(())}}]]'))
print(checkParentheses('[][][](){}'))

print(checkParentheses('([)]'))
print(checkParentheses('((()]))'))
print(checkParentheses('[{()]'))
