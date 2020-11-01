# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        carry = 0
        while l1 is not None or l2 is not None:
            current_sum = carry
            if l1:
                current_sum += l1.val
                l1 = l1.next
            if l2:
                current_sum += l2.val
                l2 = l2.next
            carry = current_sum // 10
            current.val = current_sum % 10
            if carry != 0 or l1 or l2:
                current.next = ListNode()
                current = current.next
        if carry != 0:
            current.val = carry
        return head
