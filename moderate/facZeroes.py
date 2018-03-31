'''
Count the number of zeroes in n!
'''

def facZeroes(n):
    'returns number of trailing zeroes in n!'
    power = 5
    count = 0
    while n >= power:
        count += n / power
        power *= 5

    return count

def fac(n):
    'return n!'
    if n <= 2:
        return n
    return n * fac(n-1)

def test_facZeroes():
    'test for '
    for inp in range(1, 100):
        count = facZeroes(inp)
        num = fac(inp)

        try:
            if count == 0:
                assert str(num)[-1] != '0'
            else:
                assert str(num)[-count:] == '0'*count
                assert str(num)[-(count+1):] != '0'*count
        except AssertionError:
            print 'Error in facZeroes: %s\n%s, %s' % (inp, count, num)
            return
    print 'test passed'

if __name__ == '__main__':
    test_facZeroes()

