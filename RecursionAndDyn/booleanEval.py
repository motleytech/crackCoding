'''Solution for boolean evaluation problem'''

def evaluate(exp):
    'evaluate a simple expression with an operation and 2 operands'
    if len(exp) != 3:
        raise Exception("expression length must be 3: %s" % exp)

    a, op, b = exp
    a, b = int(a), int(b)

    if op not in ['&', '|', '^']:
        raise Exception("Operation unrecognized: %s" % exp)

    if op == '&':
        return a & b
    if op == '|':
        return a | b
    if op == '^':
        return a ^ b

    raise Exception("Error evaluating expression : %s" % exp)

def countWays(k, cache2):
    'Count the number of ways to parenthesize k operations'
    if k in cache2:
        return cache2[k]
    if k <= 1:
        return 1
    nways = 0
    for x in range(0, k):
        nways += countWays(x, cache2) * countWays(k-x-1, cache2)
    cache2[k] = nways
    return nways

def handleShortcuts(nways, second, res1, op, cache2):
    'handle the simple case shortcircuits'
    # use these shortcircuits
    # 1 |
    # 0 &
    if res1[0] == 0 and op == '|':
        nways[1] += res1[1] * countWays(len(second)/2, cache2)
        return True
    elif res1[1] == 0 and op == '&':
        nways[0] += res1[0] * countWays(len(second)/2, cache2)
        return True
    return False

def countBoolEval(exp, cache1, cache2):
    'returns a dict with the numbers of parenthesizations returning 0 or 1'
    if exp in cache1:
        return cache1[exp]
    if len(exp) == 3:
        res1 = evaluate(exp)
        cache1[exp] = {1: res1, 0: 0 if res1 else 1}
        return cache1[exp]
    else:
        numOps = len(exp) / 2
        nways = {1: 0, 0: 0}
        for x in range(0, numOps):
            y = x*2 + 1
            first, op, second = exp[:y], exp[y], exp[y+1:]
            if len(first) > len(second):
                first, second = second, first
            if len(first) == 1:
                res1 = {1: int(first), 0: 1 - int(first)}
            else:
                res1 = countBoolEval(first, cache1, cache2)

            if handleShortcuts(nways, second, res1, op, cache2):
                continue

            res2 = countBoolEval(second, cache1, cache2)
            tways = sum(res1.values()) * sum(res2.values())
            if op == '|':
                nways[0] += res1[0] * res2[0]
                nways[1] += tways - res1[0] * res2[0]
            elif op == '&':
                nways[1] += res1[1] * res2[1]
                nways[0] += tways - res1[1] * res2[1]
            elif op == '^':
                bothsame = res1[0] * res2[0] + res1[1] * res2[1]
                nways[0] += bothsame
                nways[1] += tways - bothsame
        cache2[exp] = nways
        return nways

def test_countBoolEval():
    'test for countBoolEval method'
    cache1, cache2 = {}, {}
    expression = '1^0|0|1'
    result = countBoolEval(expression, cache1, cache2)
    print "%s :: %s" % (expression, result[0])
    assert result[0] == 2

    expression = '0&0&0&1^1|0'
    result = countBoolEval(expression, cache1, cache2)
    print "%s :: %s" % (expression, result[1])
    assert result[1] == 10

    print 'Test Passed'

if __name__ == '__main__':
    test_countBoolEval()

