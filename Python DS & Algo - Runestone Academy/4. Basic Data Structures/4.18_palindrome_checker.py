from deque import Deque

def palindrome_checker(str):
    deque = Deque()
    for char in str:
        deque.addRear(char)
    while deque.size() > 1:
        if deque.removeRear() != deque.removeFront():
            return False
    return True

print(palindrome_checker('hannah')) # True
print(palindrome_checker('racecar')) # True
print(palindrome_checker('yoloswaggins')) # False
