from stack import Stack

def palindrome_check(string):
    stack = Stack()
    string = string.replace(' ', '')
    for char in string:
        stack.push(char)
    reverse = ''
    while not stack.isEmpty():
        reverse += stack.pop()
    return reverse == string

print(palindrome_check('RACE CAR'))
