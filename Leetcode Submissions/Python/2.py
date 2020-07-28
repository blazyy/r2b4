'''
https://leetcode.com/problems/add-two-numbers/
64ms runtime, 13.8 MB memory
Time Complexity - O(n) Where n = no. of digits in the sum of the 2 numbers
'''


def addTwoNumbers(l1, l2):
    head = l3 = ListNode()
    carry = 0
    while l1 or l2:
        add = carry
        if l1:
            add += l1.val
            l1 = l1.next
        if l2:
            add += l2.val
            l2 = l2.next
        carry = add // 10
        l3.val = add % 10
        if l1 or l2:
            l3.next = ListNode()
        l3 = l3.next
    if carry != 0:
        l3 = ListNode(carry)
    return head


'''
# Initial Solution - 79ms runtime, 14 MB memory
# Time Complexity - O(n) Where n = no. of digits in the sum of the 2 numbers
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        multiplier = 10
        num1, num2 = l1.val, l2.val
        current1, current2 = l1, l2
        while current1.next or current2.next:
            if current1.next is not None:
                num1 = num1 + (current1.next.val * multiplier)
                current1 = current1.next
            if current2.next is not None:
                num2 = num2 + (current2.next.val * multiplier)
                current2 = current2.next
            multiplier *= 10
        add = num1 + num2
        head = return_ll = ListNode()
        while add:
            return_ll.val = add % 10
            add //= 10
            if add:
                return_ll.next = ListNode()
                return_ll = return_ll.next
        return head
'''
