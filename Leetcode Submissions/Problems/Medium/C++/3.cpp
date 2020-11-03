// # https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0, longest = 0;
        unordered_map <char, int> char_map;
        for(int i = 0; i < s.length(); i++){
            if(char_map.find(s[i]) != char_map.end())
                if(char_map[s[i]] >= start)
                    start = char_map[s[i]] + 1;
            char_map[s[i]] = i;
            longest = max(longest, i + 1 - start);
        }
        return longest;
    }
};
