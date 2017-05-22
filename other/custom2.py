from pprint import pprint as pp
from itertools import permutations

def func1():
    unused = set(range(10))
    urem = unused.remove
    uadd = unused.add
    count = 0
    for a, b in permutations(unused, 2):
        urem(a); urem(b)
        for c, d in permutations(unused, 2):
            urem(c); urem(d)
            e = a + d
            count += 1
            uadd(c); uadd(d)
        uadd(a); uadd(b)
    print 'func1 count : %s' % count

def func2():
    unused = set(range(10))
    urem = unused.remove
    uadd = unused.add
    count = 0
    for a in unused.copy():
        urem(a)
        for b in unused.copy():
            urem(b)
            for c in unused.copy():
                urem(c)
                for d in unused.copy():
                    urem(d)
                    e = a + d
                    count += 1
                    uadd(d)
                uadd(c)
            uadd(b)
        uadd(a)
    print 'func2 count : %s' % count


__builtins__.func1 = func1
__builtins__.func2 = func2

from timeit import timeit
print timeit('func1', number=100000000)
print timeit('func2', number=100000000)

