from linked_list import LinkedList
from timeit import Timer
import random

list_size = 100
number_of_tests = 100
decimal_places = 6

def ll_append(list_size):
    ll = LinkedList()
    for i in range(list_size):
        ll.append(random.randint(0, 1000))

def ll_append_using_pointer(list_size):
    ll = LinkedList()
    for i in range(list_size):
        ll.append_using_pointer(random.randint(0, 1000))

def ll_insert(list_size):
    ll = LinkedList()
    for i in range(list_size):
        ll.insert(random.randint(0, 1000), random.randint(0, ll.get_size()))

def pl_append(list_size):
    lst = []
    for i in range(list_size):
        lst.append(random.randint(0, 1000))

def pl_insert(list_size):
    lst = []
    for i in range(list_size):
        lst.insert(random.randint(0, 1000), random.randint(0, len(lst)))

#t = Timer('ll_append(list_size)', 'from __main__ import ll_append,  list_size')
#print('LL Append Times: \t\t', round(t.timeit(number_of_tests), decimal_places), 'ms')

t = Timer('ll_append_using_pointer(list_size)', 'from __main__ import ll_append_using_pointer,  list_size')
print('LL Pointer Append Times: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')

t = Timer('pl_append(list_size)', 'from __main__ import pl_append,  list_size')
print('Python List Append Times: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')


t = Timer('ll_insert(list_size)', 'from __main__ import ll_insert,  list_size')
print('Linked List Insert Times: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')

t = Timer('pl_insert(list_size)', 'from __main__ import pl_insert,  list_size')
print('Python List Insert Times: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')
