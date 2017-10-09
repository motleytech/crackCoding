
def permutations(seq):
    def _recurPerms(unused, curr):
        if len(unused) == 0:
            yield ''.join(curr)
        else:
            for x in unused.copy():
                unused.remove(x)
                curr.append(x)
                for y in _recurPerms(unused, curr):
                    yield y
                curr.pop()
                unused.add(x)

    return _recurPerms(set(seq), [])


def test_permutations():
    inp = 'sequnc'
    inp = sorted(inp)
    pgen = permutations(inp)
    for x in pgen:
        print x


if __name__ == '__main__':
    test_permutations()


