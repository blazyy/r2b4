# There are three types of edits that can be performed on strings: insert a character, remove a character, or
# replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away

# pale,  ple  -> true
# pales, pale -> true
# pale,  bale -> true
# pale,  nake -> false

# Page 60

# Solution 1
# Double for loop. Check if atleast n-1 characters from one string exists in the other
# Time Complexity: O(n^2), Space Complexity: O(1)
def one_away_1(str1, str2):
    if abs(len(str1) - len(str2)) > 1: # If the difference between lengths greater than 1, return false.
        return False
    count = 0
    for ch in str1:
        if ch in str2:
            count += 1
    higher_len = max(len(str1), len(str2))
    return count >= higher_len - 1

# Solution 2
# Hashmap. Check if atleast n-1 characters of bigger string are there in smaller string. If equal, check if more than one character difference.
# Time Complexity: O(n), Space Complexity: O(n)
def one_away_2(str1, str2):
    hashmap = {}
    for ch in str1:
        if ch not in hashmap:
            hashmap[ch] = ' '
    count = 0
    for ch in str2:
        if ch in hashmap:
            count += 1
    return max(len(str1), len(str2)) - count <= 1

# Solution 3
# Single for loop
# If more than one difference found, return false
# Time Complexity: O(n), Space Complexity: O(1)
def one_away_3(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    if len(str2) < len(str1): # str1 should be the smaller string
        str1, str2 = str2, str1
    index1 = 0
    index2 = 0
    found_diff = False
    while index1 < len(str1) and index2 < len(str2):
        if str1[index1] == str2[index2]:
            index1 += 1
        else:
            if found_diff: # Only allow one difference
                return False
            found_diff = True
            if len(str1) == len(str2):
                index1 += 1
        index2 += 1
    return True

print(one_away_1('pale', 'ple'), one_away_1('pales', 'pale'), one_away_1('pale', 'bale'), one_away_1('pale', 'bake'))
print(one_away_2('pale', 'ple'), one_away_2('pales', 'pale'), one_away_2('pale', 'bale'), one_away_2('pale', 'bake'))
print(one_away_3('pale', 'ple'), one_away_3('pales', 'pale'), one_away_3('pale', 'bale'), one_away_3('pale', 'bake'))
