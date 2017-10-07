'''draw a bitwise line from (x1, y) to (x2, y)'''

def drawLine(screen, width, x1, x2, y):
    sbyte, sbits = x1 / 8, x1 % 8
    ebyte, ebits = x2 / 8, x2 % 8

    if ebyte > sbyte:
        sbits = 7 - sbits
        while sbits >= 0:
            screen[y][sbyte] |= 1 << sbits
            sbits -= 1

        cbyte = sbyte + 1
        while cbyte < ebyte:
            screen[y][cbyte] = 255
            cbyte += 1

        ebits = 7 - ebits
        while ebits < 8:
            screen[y][ebyte] |= 1 << ebits
            ebits += 1
    else:
        sbits = 7 - sbits
        ebits = 7 - ebits
        for x in range(ebits, sbits + 1):
            screen[y][sbyte] |= 1 << x


def test_drawLine():
    for x in range(40):
        for y in range(x, 40):
            screen = [[0]*5]
            drawLine(screen, len(screen), x, y, 0)

            for row in screen:
                for col in row:
                    print '{0:08b}'.format(col),
            print ''
        print ''
    print 'Test Passed'


if __name__ == '__main__':
    test_drawLine()



