'''solution for the multisearch problem'''

def createLookup(t):
    'create a lookup structure for matching words'
    lookup = {}
    for x in t:
        curr = lookup
        for y in x:
            if y not in curr:
                curr[y] = {}
            curr = curr[y]
        curr['word'] = x
    return lookup

def findMatch(text, pos, lookup):
    'match words in text starting at pos with words in lookup'
    words = []
    curr = lookup
    p1 = pos
    while True:
        try:
            x = text[p1]
        except KeyError:
            break
        if x in curr:
            curr = curr[x]
            if 'word' in curr:
                words.append((curr['word'], pos))
        else:
            break
        p1 += 1

    return words

def search(text, t):
    'search for words from t in text'
    lookup = createLookup(t)
    allWords = []
    for pos in range(len(text)):
        words = findMatch(text, pos, lookup)
        allWords.extend(words)
    return allWords

def testSearch():
    'test for search method'
    data = ['cat', 'cam', 'cot', 'ate', 'ace', 'came']

    text = "the cat ate the cot when it came in"

    assert search(text, data) == [('cat', 4), ('ate', 8), ('cot', 16), ('cam', 28), ('came', 28)]

    print 'Passed'

if __name__ == '__main__':
    testSearch()
