'''implementation of a simple calculator'''

operMap = {
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b,
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b
}

digits = '0123456789'

opers = '+-*/'

def tokenize(exp):
    'separate expression into tokens'
    exp = exp.replace(' ', '')
    out = []

    c = 0
    lexp = len(exp)
    while True:
        if c == lexp:
            break

        if exp[c] in digits:
            num = ''
            while exp[c] in digits:
                num += exp[c]
                c += 1
                if c == lexp:
                    break
            out.append(num)

        elif exp[c] in opers:
            out.append(exp[c])
            c += 1
    return out

def calc(exp):
    'evaluate the expression'
    tokens = tokenize(exp)

    for oset in ['*/', '+-']:
        i = 0
        while i < len(tokens) - 2:
            a, b, c = [tokens[i+x] for x in range(3)]
            if b in oset:
                _ = [tokens.pop(i) for _ in range(3)]
                tokens.insert(i, operMap[b](int(a), int(c)))
            else:
                i += 2

    return tokens[0]

def test():
    'test for the calculator'
    exp = '22*3+14/6*3+15'
    assert calc(exp) == eval(exp)

    print 'Passed'

if __name__ == '__main__':
    test()
