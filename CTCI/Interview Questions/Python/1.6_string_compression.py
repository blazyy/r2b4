# Implement a method to perform basic string compression using the counts of repeated characters. For example, the string 'aabccccaaa' would become 'a2b1c4a3'. If the "compressed" string would not become smaller from the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters

# Page 60

# Solution 1
# For loop
# One downside here is that we build the string without checking if compression will actually reduce the length of the string. If the string has many non repeating character sequences, we would've wasted space by building a string which we'd never use.
# Time Complexity: O(n) Space Complexity: I don't think it makes sense to mention this here.
def compress_string_1(string):
    comp_str = [] # Using a list since python strings are immutable and therefore concatenations are costly
    comp_str.append(string[0])
    current_char = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i] == current_char:
            count += 1
        else:
            current_char = string[i]
            comp_str.append(count)
            comp_str.append(current_char)
            count = 1
    comp_str.append(count)
    if len(comp_str) >= len(string):
        return string
    return ''.join([str(ch) for ch in comp_str])

# Solution 2
# Counting the size of the compressed string beforehand so that we don't unnecessarily start creating a new string. Downsize is that it needs to iterate through the string twice. Another advantage here is that we already know the final size of the string. Although it doesn't matter in Python since lists are automatically resizing.
# Time Complexity: O(n), Space Complexity: I don't think it makes sense to mention this here.
def compress_string_2(string):
    consec_counts = count_consecutives(string)
    if consec_counts * 2 >= len(string):
        return string
    comp_str = []
    comp_str.append(string[0])
    current_char = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i] == current_char:
            count += 1
        else:
            current_char = string[i]
            comp_str.append(count)
            comp_str.append(current_char)
            count = 1
    comp_str.append(count)
    if len(comp_str) >= len(string):
        return string
    return ''.join([str(ch) for ch in comp_str])

def count_consecutives(string):
    current_char = string[0]
    consec_counts = 1
    for i in range(1, len(string)):
        if string[i] != current_char:
            current_char = string[i]
            consec_counts += 1
    return consec_counts

print(compress_string_1('aabccccaaa'))
print(compress_string_2('aabccccaaa'))
print(compress_string_1('abcdefhigj'))
print(compress_string_2('abcdefhigj'))
