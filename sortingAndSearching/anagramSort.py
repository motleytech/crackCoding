'anagram sort implementation and test'

def anagramSort(strs):
    '''sort strings by lexicographics order of
    their sorted letters - anagrams will be next
    to each other'''
    newStrs = []
    for s in strs:
        newStrs.append((sorted(s), s))
    return [x[1] for x in sorted(newStrs)]


def test_anagramSort():
    'test for anagramSort'
    strs = ['rat', 'cat', 'art', 'bat', 'tar', 'tac', 'tab']

    newStrs = anagramSort(strs)
    assert abs(newStrs.index('rat') - newStrs.index('art')) == 1
    assert abs(newStrs.index('bat') - newStrs.index('tab')) == 1

    print 'Test passed'

if __name__ == '__main__':
    test_anagramSort()
