def powers_of_n(n):
    if n <= 1:
        return 1
    prev = powers_of_n(n // 2)
    curr = prev * 2
    print(curr)
    return curr

powers_of_n(50)
