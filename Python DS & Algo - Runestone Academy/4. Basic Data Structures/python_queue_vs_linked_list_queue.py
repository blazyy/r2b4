from queue import Queue as PythonQueue
from queue_using_linkedlist import Queue as LLQueue
from timeit import Timer
import random

list_size = 100
number_of_tests = 10000
decimal_places = 6

def pqueue_enqueue(list_size):
    pqueue = PythonQueue()
    for i in range(list_size):
        pqueue.enqueue(random.randint(0, 1000))

def llqueue_enqueue(list_size):
    llqueue = LLQueue()
    for i in range(list_size):
        llqueue.enqueue(random.randint(0, 1000))

print('List Size: ', list_size, '\n')

t = Timer('pqueue_enqueue(list_size)', 'from __main__ import pqueue_enqueue, list_size')
print('Python Queue Enqueue: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')

t = Timer('llqueue_enqueue(list_size)', 'from __main__ import llqueue_enqueue, list_size')
print('LL Queue Enqeue: \t', round(t.timeit(number_of_tests), decimal_places), 'ms')
