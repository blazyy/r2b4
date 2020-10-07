# Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# Input:  Tact Coa
# Output: True (permutations: "taco cat", "atco cta". etc.)

# Page 60

# Solution 1
# Using a counter array.
# Assuming that character set only contains lowercase alphabets.
# Palindromes always have either one set of odd numbered paired letters and even numbered pairs of letters or all even numbered pairs of letters. We can use this to check whether there is more than one odd pair, in which case it is not a palindrome. This solution ignores spaces.
# Time Complexity: O(n), Space Complexity: O(1)
def is_palindrome_permutation_1(string):
    counter = [0] * 26
    for ch in string:
        if ch != ' ':
            index = ord(ch) - ord('a')
            if counter[index] == 1:
                counter[index] -= 1
            else:
                counter[index] += 1
    seen_one = False
    for ch in string:
        if ch != ' ':
            index = ord(ch) - ord('a')
            if counter[index] == 1 and not seen_one:
                seen_one = True
            elif counter[index] == 1 and seen_one:
                return False
    return True

# Solution 2
# Using a hashmap
# If the number of odd pairs are more than 1, return false
# Time Complexity: O(n), Space Complexity: O(m) where m is the number of unique characters in the string.
def is_palindrome_permutation_2(string):
    hashmap = {}
    for ch in string:
        if ch != ' ':
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1
    odd_count = 0
    for key in hashmap.keys():
        if hashmap[key] % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return odd_count <= 1

# Solution 3
# Using a bit vector
# Time Complexity: O(n), Space Complexity: O(1)
def is_palindrome_permutation_3(string):
    bit_vector = 0
    for ch in string:
        if ch != ' ':
            char_value = ord(ch) - ord('a')
            if bit_vector & (1 << char_value) == 0: # Only evaluates to zero if bit was not set
                bit_vector |= (1 << char_value)
            else:
                bit_vector &= ~(1 << char_value) #  Toggles bit which is at char_value's place
    # If a bit vector has only one 1, ANDing it with (itself - 1) will give 0. If there is more than one 1, it won't give a 0.
    return bit_vector == 0 or ((bit_vector - 1) & bit_vector) == 0
