# Devise an experiment that compares the performance of the del operator on lists and dictionaries.

import timeit
import random
for i in range(1000000, 100000100, 2000000):

    lst = list(range(i))
    diction = {j:None for j in range(i)}

    del_list_timer = timeit.Timer("del lst[random.randrange(%d)]" %i, "from __main__ import random, lst")
    del_dict_timer = timeit.Timer("del diction[random.randrange(%d)]" %i, "from __main__ import random, diction")

    del_list_time = del_list_timer.timeit(number = 1000)
    del_dict_time = del_dict_timer.timeit(number = 1000)

    print("%d\t\t\t\t\t%f\t\t\t%f" % (i, del_list_time, del_dict_time))
