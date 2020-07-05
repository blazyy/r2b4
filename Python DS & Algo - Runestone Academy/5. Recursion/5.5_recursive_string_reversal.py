# I honestly don't see the point of this program but I'm doing it anyway.
# yay recursion i guess


def rev_str(str):
    if len(str) > 1:
        return str[-1] + rev_str(str[:-1])
    return str[-1]


print(rev_str('Yoloswag'))
