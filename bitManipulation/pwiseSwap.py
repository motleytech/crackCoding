'''swap the pairwise odd and even bits (assuming 32 bits)'''

odds = 1
for x in range(1, 5):
    shift = 2 ** x
    odds = (odds << shift) + odds

evens = odds << 1

def pwiseSwap(a):
    '''swap the odd and even bits in a'''
    return ((a & odds) << 1) | ((a & evens) >> 1)

def test_pwiseSwap():
    n = 0b11001010
    assert pwiseSwap(n) == 0b11000101

    print 'Test Passed'

if __name__ == '__main__':
    test_pwiseSwap()
