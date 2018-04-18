'solution to the word distance problem'

import string

def getWords(inp):
    'return words from the input stream'
    while True:
        word = ''
        while True:
            ch = inp.read(1)
            if not ch:
                break
            if ch in string.whitespace:
                if not word:
                    continue
                break
            word += ch
        if word:
            yield word
        else:
            break

def getWordDist(inp, a, b):
    'return the min word distance between words a and b in file inp'
    posa, posb = None, None
    minDiff = None
    for i, w in enumerate(getWords(inp)):
        if w == a:
            posa = i
            if posb:
                diff = posa - posb
                if minDiff is None or diff < minDiff:
                    minDiff = diff
        if w == b:
            posb = i
            if posa:
                diff = posb - posa
                if minDiff is None or diff < minDiff:
                    minDiff = diff
    return minDiff


def test():
    'test for getWordDist method'
    import StringIO

    inp = StringIO.StringIO("""i was not surprised indeed my only wonder was that he had
    not already been mixed upon this extraordinary case which was the
    one topic of conversation through the length and breadth of england
    for a whole day my companion had rambled about the room with his
    chin upon his chest and his brows knitted charging and recharging
    his pipe with the strongest black tobacco and absolutely deaf to any
    of my questions or remarks fresh editions of every paper had been
    sent up by our news agent only to be glanced over and tossed down
    into a corner yet silent as he was i knew perfectly well what it was
    over which he was brooding there was but one problem before the
    public which could challenge his powers of analysis and that was the
    singular disappearance of the favorite for the wessex cup and the
    tragic murder of its trainer when therefore he suddenly announced
    his intention of setting out for the scene of the drama it was only
    what i had both expected and hoped for""")

    assert getWordDist(inp, 'and', 'one') == 7

    inp = StringIO.StringIO('i was and not was the we not the and '
                            'are in the elbow')

    assert getWordDist(inp, 'and', 'the') == 1

    print 'Passed'

if __name__ == '__main__':
    test()
