// https://leetcode.com/problems/add-two-numbers/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode;
        ListNode *current = head;
        int carry = 0, sum;
        while(l1 || l2){
            sum = carry;
            if(l1){
                sum += l1 -> val;
                l1 = l1 -> next;
            }
            if(l2){
                sum += l2 -> val;
                l2 = l2 -> next;
            }
            current -> val = sum % 10;
            carry = sum / 10;
            if(l1 || l2 || carry){
                current -> next = new ListNode;
                current = current -> next;
            }
        }
        if(carry)
            current -> val = carry;
        return head;
    }
};
