import random
from collections import defaultdict

def findMaxLivingYear(people):
    births = [x for x, y in people]
    deaths = [x+y+1 for x, y in people]

    bDict = defaultdict(lambda : 0)
    dDict = defaultdict(lambda : 0)

    for x in births:
        bDict[x] += 1

    for y in deaths:
        dDict[y] += 1


    alive = 0
    malive = 0
    myear = 0
    for x in range(1800, 2000):
        alive = alive + bDict[x] - dDict[x]
        if alive > malive:
            malive = alive
            myear = x

    return malive, myear

def test():
    people = [(random.randint(1800, 1900), random.randint(50, 90)) for x in range(500)]
    print findMaxLivingYear(people)

if __name__ == '__main__':
    test()
