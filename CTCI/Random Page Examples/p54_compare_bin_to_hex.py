# Write a function to check if the value of a binary number passed as a string equals the hexadecimal representation of a string

def hex_equals_bin(bin, hex):
    num_from_bin = convert_from_base(bin, 2)
    num_from_hex = convert_from_base(hex, 16)
    if num_from_bin == -1 or num_from_hex == -1:
        return False
    return num_from_bin == num_from_hex


def convert_from_base(num, base):
    if base < 2 or base > 16:
        return -1
    decimal = 0
    place = 0
    ch_index = len(num) - 1
    while ch_index >= 0:
        digit = char_to_digit(num[ch_index])
        if digit == -1 or digit >= base:
            return -1
        decimal = decimal + (base ** place) * digit
        ch_index -= 1
        place += 1
    return decimal


def char_to_digit(char):
    digit_values = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    if char not in digit_values:
        if char.isnumeric():
            return int(char)
        return -1
    return digit_values[char]

print(hex_equals_bin('100000000', '100'))
print(hex_equals_bin('11100000010', '702'))
print(hex_equals_bin('101011110011011110', '2BCDE'))
