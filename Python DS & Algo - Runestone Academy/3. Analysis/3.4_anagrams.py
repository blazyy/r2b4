# Anagrams

# I'll be implementing my own functions instead of the ones in the article because i'm bored af rn

# 1: Our first solution to the anagram problem will check the lengths of the strings and then to see that each character in the first string actually occurs in the second. If it is possible to “checkoff” each character, then the two strings must be anagrams. Checking off a character will be accomplished by replacing it with the special Python value None. However, since strings in Python are immutable, the first step in the process will be to convert the second string to a list. Each character from the first string can be checked against the characters in the list and if found, checked off by replacement. ActiveCode 1 shows this function.

def is_anagram_1(str1, str2):
    if len(str1) == len(str2):
        str1 = list(str1)
        str2 = list(str2)
        for i in range(len(str1)):
            if str1[i] in str2:
                str2[str2.index(str1[i])] = None
                str1[i] = None
        for char in str1:
            if char != None:
                return False
        return True
    return False
print(is_anagram_1('heart', 'earth'))


# 2: Another solution to the anagram problem will make use of the fact that even though s1 and s2 are different, they are anagrams only if they consist of exactly the same characters. So, if we begin by sorting each string alphabetically, from a to z, we will end up with the same string if the original two strings are anagrams. ActiveCode 2 shows this solution. Again, in Python we can use the built-in sort method on lists by simply converting each string to a list at the start.

def is_anagram_2(str1, str2):
    if len(str1) == len(str2):
        str1 = list(str1)
        str2 = list(str2)
        str1.sort()
        str2.sort()
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True
    return False
print(is_anagram_2('heart', 'earth'))

# 3: Our final solution to the anagram problem takes advantage of the fact that any two anagrams will have the same number of a’s, the same number of b’s, the same number of c’s, and so on. In order to decide whether two strings are anagrams, we will first count the number of times each character occurs. Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character. Each time we see a particular character, we will increment the counter at that position. In the end, if the two lists of counters are identical, the strings must be anagrams. ActiveCode 3 shows this solution.

def is_anagram_3(str1, str2):
    if len(str1) == len(str2):
        c1 = [0] * 26
        c2 = [0] * 26
        for char in str1:
            c1[ord(char) - ord('a')] += 1
        for char in str2:
            c2[ord(char) - ord('a')] += 1
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                return False
        return True
    return False

print(is_anagram_3('heart', 'earth'))
