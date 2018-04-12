'''solution to the pattern matching problem'''

def swapAB(pat):
    'swaps a and b in the pattern'
    patMap = {
        'a': 'b',
        'b': 'a'
    }
    return ''.join(patMap[x] for x in pat)

def match(v, p, a=None, b=None):
    'matches value to the pattern containing (a)s and (b)s'
    if v and not p:
        return False
    if not v and p:
        return False
    if not v and not p:
        return True, a, b

    if p[0] == 'a':
        if not a:
            for alen in range(1, len(v)/p.count('a') + 1):
                a = v[:alen]
                result = match(v[alen:], p[1:], a, b)
                if result:
                    return result
            return False
        if v.startswith(a):
            alen = len(a)
            return match(v[alen:], p[1:], a, b)
        return False
    if p[0] == 'b':
        if not b:
            for blen in range(1, len(v)/p.count('b') + 1):
                b = v[:blen]
                result = match(v[blen:], p[1:], a, b)
                if result:
                    return result
            return False
        if v.startswith(b):
            blen = len(b)
            return match(v[blen:], p[1:], a, b)
        return False

def matchPattern(value, pattern):
    'wrapper for match method'
    if len(pattern) <= 1:
        return True
    if pattern[0] == 'b':
        pattern = swapAB(pattern)

    if pattern == 'ab':
        if len(value) > 1:
            return True, value[0], value[1:]
        return False

    return match(value, pattern)

def test():
    'test for the pattern matching method'
    assert matchPattern('catcatgocatgo', 'aabab') == (True, 'cat', 'go')
    assert matchPattern('catcatgocatgo', 'ab') == (True, 'c', 'atcatgocatgo')
    print 'Passed'

if __name__ == '__main__':
    test()
