def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

print(gcd(60, 36))
print(gcd(35, 10))
print(gcd(99990921, 12676210))
