from stack import Stack as PythonStack
from stack_using_linkedlist import Stack as LLStack
from timeit import Timer
import random

list_size = 100
number_of_tests = 10000
decimal_places = 6

def pstack_push(list_size):
    pstack = PythonStack()
    for i in range(list_size):
        pstack.push(random.randint(0, 1000))

def llstack_push(list_size):
    llstack = LLStack()
    for i in range(list_size):
        llstack.push(random.randint(0, 1000))

print('List Size: ', list_size, '\n')

t = Timer('pstack_push(list_size)', 'from __main__ import pstack_push, list_size')
print('Python Stack Push: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')

t = Timer('llstack_push(list_size)', 'from __main__ import llstack_push, list_size')
print('LL Stack Push: \t\t', round(t.timeit(number_of_tests), decimal_places), 'ms')
