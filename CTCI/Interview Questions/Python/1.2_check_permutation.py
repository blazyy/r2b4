# Check permutation: Given two strings, write a method to decided if one is a permutation of the other.
# Page 60

# Solution 1:
# Sorting both strings and checking if they are equal.
# Time Complexity: O(n log n), Space Complexity: O(1)
def check_permutation_1(str1, str2):
    if len(str1) != len(str2):
        return False
    if(sorted(str1) == sorted(str2)):
        return True
    return False

# Solution 2:
# Having a counter array for each string, and comparing all values in these counter arrays.
# Assuming characters are ASCII, so character set is 128 long.
# Time Complexity: O(n), Space Complexity: O(1) sinced charset is always of fixed length.
def check_permutation_2(str1, str2):
    if len(str1) != len(str2):
        return False
    charset_length = 128
    counter = [0] * charset_length
    for i in range(len(str1)):
        counter[ord(str1[i]) - ord('a')] += 1
    for i in range(len(str2)):
        counter[ord(str2[i]) - ord('a')] -= 1
        if counter[ord(str2[i]) - ord('a')] < 0:
            return False
    return True

# Solution 3
# Using a hashmap to store character counts. Using a hashmap here seems unnecessary but why the heck not?
# Time Complexity: O(n), Space Complexity: O(n)
def check_permutation_3(str1, str2):
    if(len(str1) != len(str2)):
        return False
    char_counts = {}
    for ch in str1:
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
    for ch in str2:
        if ch not in char_counts:
            return False
        char_counts[ch] -= 1
        if char_counts[ch] < 0:
            return False
    return True
