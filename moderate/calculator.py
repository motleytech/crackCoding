

def tokenize(exp):
    exp = exp.replace(' ', '')
    out = []

    c = 0
    lexp = len(exp)
    while True:
        if c == lexp:
            break

        if exp[c] in '0123456789':
            num = ''
            while exp[c] in '0123456789':
                num += exp[c]
                c += 1
                if c == lexp:
                    break

            out.append(num)
        elif exp[c] in '+-/*':
            out.append(exp[c])
            c += 1
    return out


def calc(exp):
    tokens = tokenize(exp)

    res = []
    ltokens = len(tokens)
    i = 0
    while i < ltokens - 2:
        a, b, c = tokens[i], tokens[i+1], tokens[i+2]
        if b == '*':
            res.append(object)







def test():
    exp = '22*3+5/6*3+15'
    print tokenize(exp)

if __name__ == '__main__':
    test()
