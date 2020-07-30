/**
https://leetcode.com/problems/reverse-integer/
0ms runtime, 6.1 MB memory
Time Complexity - O(n) Where n = no. of digits in the number
**/

class Solution {
public:
    int reverse(int x) {
        int rem, rev_x = 0;
        while(x){
            rem = x % 10;
            if(rev_x > INT_MAX / 10 or rev_x < INT_MIN /10)
                return 0;
            rev_x = rev_x * 10 + rem;
            x /= 10;
        }
        return rev_x;
    }
};
