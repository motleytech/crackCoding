'''
Compress a string by returning the run length encoded version.
If the RLE string is not smaller, return original string
'''


def compress(s):
    '''
    return run length encoding of s (if rle(s) is smaller than s)
    '''
    result = ''
    index = 0
    while index < len(s):
        curr = s[index]
        offset = index + 1
        count = 1
        while offset < len(s) and s[offset] == curr:
            count += 1
            offset += 1
        result += curr + str(count)
        index += count
    return result if len(result) < len(s) else s


def test_compress():
    '''
    tests for compress method
    '''
    print 'Testing compress...',
    assert compress('aa') == 'aa'
    assert compress('aaa') == 'a3'
    assert compress('aaabbccdddd') == 'a3b2c2d4'
    assert compress('') == ''
    assert compress('string') == 'string'
    print 'Passed'

if __name__ == '__main__':
    test_compress()

