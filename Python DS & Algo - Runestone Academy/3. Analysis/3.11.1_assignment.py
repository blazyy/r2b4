# Devise an experiment to verify that the list index operator is O(1)
from timeit import Timer

a = list(range(1000000))
b = list(range(10000000))
c = list(range(100000000))
d = list(range(1000000000))

idx_a = timeit.Timer("a.index(len(a)-1)", "from __main__ import x")
idx_b = timeit.Timer("a.index(len(b)-1)", "from __main__ import x")
idx_c = timeit.Timer("a.index(len(c)-1)", "from __main__ import x")
idx_d = timeit.Timer("a.index(len(d)-1)", "from __main__ import x")

print('a: {}'.format(idx_a.timeit()))
print('b: {}'.format(idx_b.timeit()))
print('c: {}'.format(idx_c.timeit()))
print('d: {}'.format(idx_d.timeit()))
