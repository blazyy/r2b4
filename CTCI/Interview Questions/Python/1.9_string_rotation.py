# Assume you have a mthod isSubstring which cheks if one word is a substring of another. Given two strings s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.

# Example: "waterbottle" is a rotation of "erbottlewa"

# Page 61

# Solution
# Double s1 and check if s2 in s1 using isSubstring
# waterbottle -> waterbottlewaterbottle. 'erbottlewa' exists in doubled s1.
# Time Complexity: O(n), Space Complexity: O(n)
def is_string_rotation(s1, s2):
    return s2 in s1 * 2

print(is_string_rotation('waterbottle', 'erbottlewa'))
print(is_string_rotation('waterbottle', 'erbottlea'))
