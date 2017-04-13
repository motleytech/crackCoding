'''
Check if the 2 given strings are just 1 or 0 differences away
A difference is defined as 1 character missing or 1 character different

This implies that
1. The lengths of the 2 strings can at most differ by 1
2. If strings have different length, we compare the larger with the smaller string,
while skipping at most 1 difference.
3. If strings are same length, character by character comparison should at most
have one difference.
'''

def areOneAway(s1, s2):
    '''
    Returns True if s1 and s2 are just one
    edit (add, delete or modify one char) away.
    '''
    s1, s2 = (s1, s2) if len(s1) > len(s2) else (s2, s1)
    ls1, ls2 = map(len, (s1, s2))
    if ls1 == ls2:
        ndiffs = sum(0 if a == b else 1 for a, b in zip(s1, s2))
        if ndiffs > 1:
            return False
        return True
    if ls1 == ls2 + 1:
        skipped = False
        idx1, idx2 = 0, 0
        while idx2 < ls2:
            if s1[idx1] == s2[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                if not skipped:
                    skipped = True
                    idx1 += 1
                    continue
                return False
        return True
    return False


def test_areOneAway():
    '''Test for areOneAway method'''
    print 'Testing areOneAway... ',
    assert areOneAway('pale', 'ple')
    assert areOneAway('pales', 'pale')
    assert not areOneAway('pale', 'bake')
    assert areOneAway('pale', 'bale')
    print 'Passed'


if __name__ == '__main__':
    test_areOneAway()


