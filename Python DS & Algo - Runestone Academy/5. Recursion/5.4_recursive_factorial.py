def recursive_factorial(num):
    return 1 if num <= 1 else num * recursive_factorial(num - 1)


print(recursive_factorial(5))
