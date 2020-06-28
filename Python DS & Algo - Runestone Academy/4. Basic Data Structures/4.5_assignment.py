from stack import Stack

# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

def revstring(mystr):
    stack = Stack()
    mystr = list(mystr)
    for char in mystr:
        stack.push(char)
    output = []
    while not stack.isEmpty():
        output.append(stack.pop())
    return ''.join(output)

print(revstring('faaezrazeen'))
