'solution for the longest word problem'

def isACombination(w, ws):
    'checks if w can be split into multiple words. Returns number of words'
    for i in range(1, len(w)):
        s = w[:i]
        if s in ws:
            rest = w[i:]
            if rest in ws:
                return 2
            c = isACombination(rest, ws)
            if c > 0:
                return c + 1
    return 0


def getLongestCombWord(words):
    'return the longest word in words that formed by comb of other words'
    words = sorted(words, key=len, reverse=True)
    wordSet = set(words)

    for w in words:
        num = isACombination(w, wordSet)
        if num > 0:
            return w, num

    return None

def test():
    'test for getLongestCombWord'
    inp = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
    assert getLongestCombWord(inp) == ('dogwalker', 2)

    inp = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker']
    assert getLongestCombWord(inp) is None

    print 'Passed'

if __name__ == '__main__':
    test()
