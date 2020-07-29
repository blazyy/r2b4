'''
https://leetcode.com/problems/longest-substring-without-repeating-characters
56ms runtime, 13.9 MB memory
Time Complexity - O(n) where n = length of string and m is the charset
Space Complexity - O(min(m, n)) where m = size of character set
'''


def lengthOfLongestSubstring(s):
    char_map = {}
    length = start = 0
    for i, ch in enumerate(s):
        if ch in char_map:
            if char_map[ch] >= start:
                start = char_map[ch]+1
        length = max(length, i+1-start)
        char_map[ch] = i
    return length


print(lengthOfLongestSubstring('pwwkew'))  # 3
print(lengthOfLongestSubstring('abcabcbb'))  # 3
print(lengthOfLongestSubstring('dvdf'))  # 3
print(lengthOfLongestSubstring('bbbbb'))  # 1
print(lengthOfLongestSubstring(' '))  # 1


'''
# Initial Solution - 116 ms runtime, 14 MB memory
# Time Complexity - O(n) Where n = length of string
# Space Complexity - O(min(m, n)) where m = size of character set

def lengthOfLongestSubstring(s):
    start = end = count = highest = 0
    char_set = set()
    while end < len(s):
        if s[end] not in char_set:
            char_set.add(s[end])
            end += 1
            highest = max(highest, len(char_set))
        else:
            char_set.remove(s[start])
            start += 1
    return highest
'''
