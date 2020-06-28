num = int(input("Enter a positive number: "))
if num < 0:
    raise RuntimeError("I said a positive number!")
else:
    print("Thanks.")
