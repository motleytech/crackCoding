'modifies input array into peaks and valleys'

def peaksAndValleys(inp):
    'sort inp into peaks and valleys'
    x, y = inp[:2]
    pv = x >= y # if x >= y, starting is a peak, else valley

    for i in range(len(inp) - 2):
        x, y, z = inp[i], inp[i+1], inp[i+2]

        if pv:
            if y > z:
                inp[i+1], inp[i+2] = inp[i+2], inp[i+1]
        else:
            if y < z:
                inp[i+1], inp[i+2] = inp[i+2], inp[i+1]
        pv = not pv

    return inp


def test_peaksAndValleys():
    'test for peaksAndValleys method'
    import random
    #random.seed(1)

    inp = [random.randint(0, 1000) for _ in range(20)]

    res = peaksAndValleys(inp)
    for i, v in enumerate(zip(res, res[1:], res[2:])):
        x, y, z = v
        assert (y - x) * (z - y) <= 0, "\ni = %s, v = %s\n%s" % (i, v, res)

    print 'Test Passed'

if __name__ == '__main__':
    test_peaksAndValleys()


