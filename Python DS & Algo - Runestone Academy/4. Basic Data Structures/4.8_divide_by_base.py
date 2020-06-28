from stack import Stack

def divide_by_base(decimal, base):
    stack = Stack()
    digits = '0123456789ABCDEF'
    while decimal:
        rem = decimal % base
        stack.push(rem)
        decimal = decimal // base
    result = ''
    while not stack.isEmpty():
        result += digits[stack.pop()]
    return result

print(divide_by_base(25, 2)) # 11001
print(divide_by_base(256, 16)) # 100
print(divide_by_base(25, 8)) # 31
print(divide_by_base(233, 8)) # 351
print(divide_by_base(233, 16)) # E9
