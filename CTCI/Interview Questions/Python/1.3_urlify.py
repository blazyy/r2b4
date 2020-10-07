# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given
#  the "true" length of the string. (Note: If implementing in Java, please use a character
# array so that you can perform this operation in place)

# Page 60

# Input:  "Mr John Smith     ", 13
# Output: "Mr%20John%20Smith"

# Working backwards from the end of string, since there's extra spaces and we don't have to worry about overrwriting any characters.
# First, calculate the index from where to start rewriting from by adding true length and 2 * original spaces in the 'true' string
# Starting from this index, if a space occurs, replace with '%20', else replace with character of index i where i starts from true length - 1and goes till 0
# Time Complexity: O(n), Space Complexity: O(1)
def urlify(string, true_length):
    string = [ch for ch in string] # Doing this because strings are immutable in Python
    space_count = 0
    for i in range(true_length):
        if string[i] == ' ':
            space_count += 1
    index = true_length + space_count * 2
    for i in range(true_length - 1, -1, -1):
        if string[i] == ' ':
            string[index - 1] = '0'
            string[index - 2] = '2'
            string[index - 3] = '%'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    return ''.join(string)

print(urlify('Mr John Smith     ', 13))
