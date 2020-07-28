/**
https://leetcode.com/problems/add-two-numbers/
24ms runtime, 70.1 MB memory
Time Complexity - O(n) Where n = no. of digits in the sum of the 2 numbers
**/

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        struct ListNode * head = new ListNode;
        struct ListNode * l3 = head;
        int add, carry = 0;
        while(l1 || l2){
            add = carry;
            if(l1){
                add += l1 -> val;
                l1 = l1 -> next;
            }
            if(l2){
                add += l2 -> val;
                l2 = l2 -> next;
            }
            carry = add / 10;
            l3 -> val = add % 10;
            if(l1 || l2){
                l3 -> next = new ListNode;
                l3 = l3 -> next;
            }
        }
        if(carry)
            l3 -> next = new ListNode(carry);
        return head;
    }
};
