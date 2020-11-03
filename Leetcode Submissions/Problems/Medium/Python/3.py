# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    start = longest = 0
    for i, ch in enumerate(s):
        if ch in char_map:
            if char_map[ch] >= start:
                start = char_map[ch] + 1
        longest = max(longest, i + 1 - start)
        char_map[ch] = i
    return longest

# print(lengthOfLongestSubstring("abcabcbb")) # 3
# print(lengthOfLongestSubstring("pwwkew")) # 3
# print(lengthOfLongestSubstring("dvdf")) # 3
# print(lengthOfLongestSubstring("asjrgapa")) # 6

# O(n). Good but can do a little better.
# def lengthOfLongestSubstring(s: str) -> int:
#     a_pointer = b_pointer = longest = 0
#     seen = set()
#     while b_pointer < len(s):
#         if s[b_pointer] not in seen:
#             seen.add(s[b_pointer])
#             b_pointer += 1
#             longest = max(longest, len(seen))
#         else:
#             seen.remove(s[a_pointer])
#             a_pointer += 1
#     return longest

# # Initial solution. Bad. O(n^2).
# def lengthOfLongestSubstring(s: str) -> int:
#     seen = set()
#     count = highest = 0
#     for i in range(len(s)):
#         j = i
#         while j < len(s):
#             if s[j] not in seen:
#                 seen.add(s[j])
#                 count += 1
#                 j += 1
#             else:
#                 if count > highest:
#                     highest = count
#                 count = 0
#                 seen = set()
#                 break
#     return max(highest, count)
