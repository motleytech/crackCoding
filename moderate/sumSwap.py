'solution for sum swap problem'

def findSwapPair(a, b):
    '''
    find pair of numbers to swap in a, b such that
    swapping these numbers will make the sum of a
    and b the same
    '''
    s1, s2 = sum(a), sum(b)

    diff = s1 - s2
    if diff % 2:
        # if difference is odd, solution impossible
        return None
    diff = diff / 2

    seta = set(a)
    for x in b:
        if x + diff in seta:
            return (x+diff, x)
    return None

def test():
    'test for findSwapPair method'
    a = [4, 1, 2, 1, 1, 2]
    b = [3, 6, 7, 9]
    print findSwapPair(a, b)

if __name__ == '__main__':
    test()
