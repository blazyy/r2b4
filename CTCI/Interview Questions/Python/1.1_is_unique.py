# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# Solution 1:
# Using a hashmap.
# Time complexity: O(n), Space Complexity: O(n)
def is_unique_1(string):
    # If string contains more characters than the number of actual ASCII characters, return false.
    # If extended ASCII, it's 256 characters. If unicode, it's 2^21.
    if len(string) > 128:
        return False
    hashmap = {}
    for ch in string:
        if ch in hashmap:
            return False
        hashmap[ch] = ' '
    return True

# Solution 2:
# Sorting the input string.
# Time Complexity: O(n log n), Space Complexity: O(1).
# Note: Modifies input string.
def is_unique_2(string):
    if len(string) > 128:
        return False
    string = ''.join([ch for ch in sorted(string)])
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

# Solution 3.
# Using a character set. Here, assuming string has only lowercase alphabets but this can be extended as needed.
# Time Complexity: O(n), Space Complexity: 0(1) if fixed character set, else O(c) or O(min(c, n)) where c is the size of character set.
def is_unique_3(string):
    if len(string) > 128:
        return False
    char_set = [False] * 26
    for char in string:
        if char_set[ord(char) - ord('a')]:
            return False
        char_set[ord(char) - ord('a')] = True
    return True


# Solution 4:
# Using a bit vector (i.e. an int) and bit shifting.
# Time Complexity: O(n), Space Complexity: O(1).
# Only works for smallercase A-Z since integer can only hold 32 bits. (Python's int is unbounded but we will assume it can only hold 32 bits)
def is_unique_4(string):
    checker = 0
    for ch in string:
        value = ord(ch) - ord('a')
        # If the place of 1 in the binary representation (1 << value) matches the place of 1 at checker, the AND operation will return a 1 in that place.
        # This means the number returned by the AND operation won't be a 0, which means the current character already existed.
        if checker & (1 << value) > 0:
            return False
        checker |= (1 << value)
    return True
