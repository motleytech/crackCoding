def myfunc():
    unused = set(range(10))
    urem = unused.remove
    uadd = unused.add
    udiff = unused.difference
    ucopy = unused.copy
    set0 = set([0])

    for n in ucopy():
        urem(n)
        for e in ucopy():
            urem(e)
            for c in udiff(set0):
                urem(c)
                for t in udiff(set0):
                    urem(t)
                    for s in udiff(set0):
                        urem(s)
                        sm1 = n*9 + e*4 + c*2 + s
                        a = ( - sm1) % 10
                        if a in unused and a != 0:
                            urem(a)
                            sm = (sm1 + t + a) / 10
                            for o in udiff(set0):
                                urem(o)
                                for i in udiff(set0):
                                    urem(i)
                                    sm1 = (sm + o*8 + i*4 + t*3 + n + a)
                                    r = (n - sm1) % 10
                                    if r in unused:
                                        urem(r)
                                        sm = (sm1 + r) / 10

                                        sm = (sm + i*10 + a*3 + e*2 + t + s + n)
                                        if a == sm % 10:

                                            sm = (sm /10 + t*10 + a*3 + o*2 + r + i + c)
                                            if r == sm % 10:
                                                sm = sm / 10
                                                for p in udiff(set0):
                                                    urem(p)
                                                    sm = (sm + p*6 + r*3 + i*2 + a*3 + n + s + o + e)
                                                    if i == sm % 10:
                                                        sm = (sm/10 + i*4 + c*3 + o*3 + t*3 + e*2 + p + r*2)
                                                        if p == sm % 10:
                                                            sm = (sm/10 + s*3 + c*3 + o*3 + i*3 + r*3 + p*2 + a)
                                                            if s == sm % 10:
                                                                sm = (sm/10 + r*3 + c*3 + p*3 + s*2 + o*2 + e*2 + t + n + i)
                                                                if r == sm % 10:
                                                                    sm = (sm/10 + s*8 + e*3 + t*3 + p + a + o + n)
                                                                    if e == sm % 10:
                                                                        sm = (sm/10 + o*4 + p*2 + e*2 + n*2 + c*2 + t*2 + a*2 + i + r)
                                                                        if p == sm % 10:
                                                                            sm = (sm/10 + r*7 + n*3 + a*2 + p + c + o + s + e + t)
                                                                            if i == sm % 10:
                                                                                sm = (sm/10 + p*6 + i*3 + a*2 + n*2 + t + c + o + s + r)
                                                                                if t == sm % 10:
                                                                                    sm = (sm/10 + o + i + t)
                                                                                    if n == sm % 10:
                                                                                        sm = (sm / 10 + c)
                                                                                        if a == sm % 10 and sm < 10:
                                                                                            return {'a': a, 'c': c, 'e': e, 'i': i, 'n': n, 'o': o, 'p': p, 'r': r, 's': s, 't': t}
                                                    uadd(p)
                                        uadd(r)
                                    uadd(i)
                                uadd(o)
                            uadd(a)
                        uadd(s)
                    uadd(t)
                uadd(c)
            uadd(e)
        uadd(n)
    return "not solved"

from time import time

st = time()
print myfunc()
print 'elapsed time : %s' % (time() - st)


values = {'a': 5, 'c': 4, 'e': 9, 'i': 6, 'o': 2, 'n': 7, 'p': 3, 's': 8, 'r': 0, 't': 1}

