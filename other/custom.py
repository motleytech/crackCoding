from pprint import pprint as pp

prob = ['apperception', 'aristocratic', 'concessionaire', 'conscription',
 'inappropriate', 'incapacitate', 'inconsistent',
 'interception', 'osteoporosis', 'perspiration', 'prescription',
 'proscription', 'prosopopoeia', 'protectorate', 'protestation',
 'statistician', 'transoceanic', 'transpiration', 'antiperspirant']


program = """
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
                        sm = n*9 + e*4 + c*2 + s + t
                        a = (t - sm) % 10
                        if a in unused and a != 0:
                            urem(a)
                            sm = (sm + a) / 10
                            for o in udiff(set0):
                                urem(o)
                                for i in udiff(set0):
                                    urem(i)
                                    sm = (sm + o*8 + i*4 + t*3 + n + a)
                                    r = (n - sm) % 10
                                    if r in unused:
                                        urem(r)
                                        sm = (sm + r) / 10

                                        sm = (sm + i*10 + a*3 + e*2 + t + s + n)
                                        if a == sm % 10:
                                            sm = (sm/10 + t*10 + a*3 + o*2 + r + i + c)
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

print myfunc()
"""

rprob = [x[::-1] for x in prob]

lhs = rprob[:-1]
rhs = rprob[-1]

neqns = len(rhs)
equations = [[(rprob[y][x] if len(rprob[y]) > x else None) for y in range(len(rprob))]for x in range(neqns)]

print equations

firsts = set([p[0] for p in prob])
chEqns = []
used = set([None])
for eqn in equations:
    curr = []
    chEqns.append(curr)
    for ch in eqn:
        if ch not in used:
            curr.append((ch, eqn.count(ch)))
            used.add(ch)

for i, curr in enumerate(chEqns):
    chEqns[i] = sorted(curr, key=lambda x: x[1], reverse=True)

chEqns2 = []
for eqn in equations:
    curr = []
    chEqns2.append(curr)
    eqn = eqn[:]
    while len(eqn) > 0:
        ch = eqn[0]
        curr.append((ch, eqn.count(ch)))
        while ch in eqn:
            eqn.remove(ch)

for i, curr in enumerate(chEqns2):
    chEqns2[i] = (i+1, sorted(curr, key=lambda x: x[1], reverse=True))


pp(chEqns)
pp(chEqns2)
pp(firsts)
pp(rhs)
pp(used)

values = {'a': 5, 'c': 4, 'e': 9, 'i': 6, 'o': 2, 'n': 7, 'p': 3, 's': 8, 'r': 0, 't': 1}

exec program

