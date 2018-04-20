
'solution for the histogram volume problem'

def histVolume(data):
    'return the volume in the histogram'
    volume = 0
    maxp = data.index(max(data))

    cmax = 0
    for x in data[:maxp]:
        if x > cmax:
            cmax = x
            continue
        volume += cmax - x

    cmax = 0
    for x in data[len(data)-1:maxp:-1]:
        if x > cmax:
            cmax = x
            continue
        volume += cmax - x

    return volume

def test():
    'test for method histVolume'
    data = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]

    res = histVolume(data)
    assert res == 26

if __name__ == '__main__':
    test()
    print 'Passed'
