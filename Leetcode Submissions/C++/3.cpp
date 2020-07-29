/**
https://leetcode.com/problems/longest-substring-without-repeating-characters/
48ms runtime, 8.6 memory
Time Complexity - O(n) Where n = no. of digits in the sum of the 2 numbers
Space Complexity - O(min(m, n)) where m = size of character set
**/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0, length = 0;
        unordered_map <char, int> map;
        for(int i=0; i<s.length(); i++){
            if(map.find(s[i]) != map.end()){
                if(map[s[i]] >= start)
                    start = map[s[i]]+1;
            }
            length = max(length, i+1-start);
            map[s[i]] = i;
        }
        return length;
    }
};
