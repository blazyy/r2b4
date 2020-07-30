'''
https://leetcode.com/problems/reverse-integer/
44ms runtime, 13.8MB memory
Time Complexity - O(n) Where n = no. of digits in the number
'''


def reverse(self, x: int) -> int:
    neg = False
    if x < 0:
        neg = True
        x = abs(x)
    rev_x = 0
    while x:
        if rev_x > (2**31-1)//10 or rev_x < (-2**31)//10:
            return 0
        rem = x % 10
        rev_x = rev_x * 10 + rem
        x //= 10
    if neg:
        return -rev_x
    else:
        return rev_x


print(reverse(-123))
