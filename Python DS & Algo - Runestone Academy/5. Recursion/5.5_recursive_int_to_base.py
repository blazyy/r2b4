def int_to_base(num, base):
    digits = '0123456789ABCDEF'
    if num < base:
        return digits[num]
    else:
        return int_to_base(num//base, base) + digits[num % base]


print(int_to_base(980, 16))
