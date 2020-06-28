# Devise an experiment to verify that get item and set item are O(1) for dictionaries.
import timeit
import random
for i in range(1000000, 100000100, 2000000):

    get_timer = timeit.Timer("random.randrange(%d) in x" %i, "from __main__ import random, x")
    set_timer = timeit.Timer("x[random.randrange(%d)] = 'lol'" %i, "from __main__ import random, x")

    x = {j:None for j in range(i)}

    get_time = get_timer.timeit(number = 1000)
    set_time = set_timer.timeit(number = 1000)

    print("%d\t\t\t\t\t%f\t\t\t%f" % (i, get_time, set_time))
