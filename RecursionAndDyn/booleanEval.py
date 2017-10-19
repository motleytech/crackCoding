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


def countBoolEval(exp, cache1, cache2):
    'returns a dict with the numbers of parenthesizations returning 0 or 1'
    if exp in cache1:
        return cache1[exp]
    if len(exp) == 3:
        res = evaluate(exp)
        cache1[exp] = {1: res, 0: 0 if res else 1}
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
                if first == '1':
                    res1 = {1: 1, 0: 0}
                else:
                    res1 = {1: 0, 0: 1}
            else:
                # evaluate first and second and merge results
                res1 = countBoolEval(first, cache1, cache2)

            # use these shortcircuits
            # 1 |
            # 0 &
            done = False
            if res1[0] == 0 and op == '|':
                nways[1] += res1[1] * countWays(len(second)/2, cache2)
                done = True
            elif res1[1] == 0 and op == '&':
                nways[0] += res1[0] * countWays(len(second)/2, cache2)
                done = True
            if done:
                continue

            res2 = countBoolEval(second, cache1, cache2)
            res1c, res2c = sum(res1.values()), sum(res2.values())
            if op == '|':
                bothzero = res1[0] * res2[0]
                nways[0] += bothzero
                nways[1] += res1c * res2c - bothzero
            elif op == '&':
                bothone = res1[1] * res2[1]
                nways[1] += bothone
                nways[0] += res1c * res2c - bothone
            elif op == '^':
                bothsame = res1[0] * res2[0] + res1[1] * res2[1]
                nways[0] += bothsame
                nways[1] += res1c * res2c - bothsame
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

