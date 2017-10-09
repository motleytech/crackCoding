
'''print out all valid combinations of n paren pairs'''

def parens(a, b, curr):
    'recursively find all valid parens combinations'
    if b == 0:
        yield ''.join(curr)
    elif a < b:
        if a > 0:
            curr.append('(')
            for x in parens(a-1, b, curr):
                yield x
            curr.pop()

        curr.append(')')
        for x in parens(a, b-1, curr):
            yield x
        curr.pop()
    else:
        curr.append('(')
        for x in parens(a-1, b, curr):
            yield x
        curr.pop()


def test_parens():
    'test for parens method'
    N = 3
    assert len(list(y for y in parens(N, N, []))) == 5

    N = 4
    assert len(list(y for y in parens(N, N, []))) == 14

    print 'Test Passed'

if __name__ == '__main__':
    test_parens()




