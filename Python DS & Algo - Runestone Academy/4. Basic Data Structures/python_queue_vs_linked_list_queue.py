from queue import Queue as PythonQueue
from queue_using_linkedlist import Queue as LLQueue
from timeit import Timer
import random

lst_size = 100
n_tests = 10000
dp = 6


def p_enqueue(lst_size):
    pqueue = PythonQueue()
    for i in range(lst_size):
        pqueue.enqueue(random.randint(0, 1000))


def ll_enqueue(lst_size):
    llqueue = LLQueue()
    for i in range(lst_size):
        llqueue.enqueue(random.randint(0, 1000))


print('List Size: ', lst_size, '\n')

t = Timer('p_enqueue(lst_size)', 'from __main__ import p_enqueue, lst_size')
print('Python Enqueue: ', round(t.timeit(n_tests), dp), 'ms')

t = Timer('ll_enqueue(lst_size)', 'from __main__ import ll_enqueue, lst_size')
print('LL Enqeue: \t', round(t.timeit(n_tests), dp), 'ms')
