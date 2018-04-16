'count number of 2s appearing in all numbers between 0 and num'

def count2Brute(num):
    'brute force method to count 2s'
    count = 0
    for x in range(num + 1):
        count += str(x).count('2')

    return count

def count2s(num):
    'faster way to count 2s'
    count = 0
    p1, p2 = 0, 1
    while num > p2:
        p1, p2 = p2, p2*10
        count += ((p1 * (num / p2)) +
                  (p1 if (num % p2) / p1 > 2 else 0) +
                  ((num % p1 + 1) if (num % p2) / p1 == 2 else 0))
    return count

def test():
    'test for count2s method'
    from random import randint, seed

    seed(200)

    for x in range(1, 500):
        assert count2Brute(x) == count2s(x)

    for x in range(20):
        val = randint(1000, 3000)
        assert count2Brute(val) == count2s(val)

    print 'Passed'

if __name__ == '__main__':
    test()
