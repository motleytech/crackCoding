'''find number of bits that need to be flipped to
convert A to B'''


def count1Bits(c):
    '''returns number of 1 bits in c'''
    count = 0
    while c:
        c = (c & (c - 1))
        count += 1
    return count

def bits2Convert(a, b):
    '''return number of bit flips required to convert a -> b'''
    return count1Bits(a ^ b)

def test_bits2Convert():
    '''test for bits2Convert method'''
    assert bits2Convert(29, 15) == 2
    print 'Test passed'

if __name__ == '__main__':
    test_bits2Convert()

