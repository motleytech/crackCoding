from pprint import pprint as pp
from math import log
from time import time

problems = dict(
    easy = {
        '000000000079050180800000007007306800450708096003502700700000005016030420000000000': '345871269279653184861429537197346852452718396683592741738264915516937428924185673',
        '000000080800701040040020030374000900000030000005000321010060050050802006080000000': '761543289832791645549628137374215968128936574695487321417369852953872416286154793',
        '000000085000210009960080100500800016000000000890006007009070052300054000480000000': '132649785758213649964785123543897216276531894891426537619378452327154968485962371',
        '000700800006000031040002000024070000010030080000060290000800070860000500002006000': '159743862276589431348612759624978315917235684583164297435821976861497523792356148',
        '000900002050123400030000160908000000070000090000000205091000050007439020400007000': '814976532659123478732854169948265317275341896163798245391682754587439621426517983',
        '030000080009000500007509200700105008020090030900402001004207100002000800070000090': '235761489419328576867549213746135928521896734983472651394287165652913847178654392',
        '040000050001943600009000300600050002103000506800020007005000200002436700030000040': '348267951571943628269185374697351482123874596854629137415798263982436715736512849',
        '100920000524010000000000070050008102000000000402700090060000000000030945000071006': '176923584524817639893654271957348162638192457412765398265489713781236945349571826',
        '300200000000107000706030500070009080900020004010800050009040301000702000000008006': '351286497492157638786934512275469183938521764614873259829645371163792845547318926',
        '630000000000500008005674000000020000003401020000000345000007004080300902947100080': '639218457471539268825674139564823791793451826218796345352987614186345972947162583'
        },

    medium = {
        '000014000030000200070000000000900030601000000000000080200000104000050600000708000': '962314857134587269578296413847962531651873942329145786285639174793451628416728395',
        '080004050000700300000000000010085000600000200000040000302600000000000041700000000': '986324157124759368537861429413285976695173284278946513342617895869532741751498632',
        '083400000000070050000000000040108000000000027000300000206050000500000800000000100': '783465219421973658965281734347128596198546327652397481216854973534719862879632145',
        '098010000200000060000000000000302050084000000000600000000040809300500000000000100': '498716523257839461136425987971382654684157392523694718765241839319578246842963175',
        '600302000010000050000000000702600000000000084300000000080150000000080200000000700': '654312879913876452827495136742638591165729384398541627286157943471983265539264718',
        '600302000040000010000000000702600000000000054300000000080150000000040200000000700': '615382479943765812827491536752634198168279354394518627286157943579843261431926785',
        '600302000040000080000000000702600000000000054300000000080150000000080200000000700': '618342579943765182527891436752634891861279354394518627286157943179483265435926718',
        '600302000050000010000000000702600000000000054300000000080150000000040200000000700': '614382579953764812827591436742635198168279354395418627286157943579843261431926785',
        '602050000000003040000000000430008000010000200000000700500270000000000081000600000': '682154379951763842374892165437528916816937254295416738568271493729345681143689527',
        '602050000000004030000000000430008000010000200000000700500270000000000081000600000': '682153479951764832374892165437528916816947253295316748568271394729435681143689527'
        },
    hard = {
        '000000061890000000000000000000520400000030000060000000530006070200000800000107000': '724895361895361742613472589187529436452638197369714258531286974276943815948157623',
        '000050700400000600000001000000060002300900000000000050065000100070400000000003080': '938256741417398625526741893789564312351982476642137958265879134873415269194623587',
        '000200800970000000000000000000106200400000100090000000001570000000040009600000030': '534291876978465321216738945783156294462987153195324768341579682827643519659812437',
        '000570600310000000000000000400103000070400000000000200207060000000008010000000005': '948572631312846579765319428426193857873425196591687243257961384634758912189234765',
        '001000800500000000000070000000500108730020000000000400040608000600000020000100000': '271963845593814267864275319426539178738421956915786432142658793689347521357192684',
        '041000000000807000000200000000004800800000500000090000000030096060000040700500000': '241965378935817462687243951376154829819672534452398617528431796163789245794526183',
        '200000001004030000800000000070600050100002000000000400008000590030010000000200000': '253867941764139825891524367479681253185342679326795418618473592532916784947258136',
        '500000120000400000000000300650000700000200009100000000300080010007300000000000004': '543897126281436975976152348652943781738261459194578263329684517467315892815729634',
        '600130000004000800000000000007500000000020060080000030000400709300001000020000000': '672138954514692873893745216437586192951327468286914537168453729349271685725869341',
        '830400000000010050000000000005070300000000607100000000070602000009000010000800000': '836425179794316852512789436965278341328154697147963528471632985689547213253891764'
    })


range9 = range(9)
range81 = range(81)
powersOf2 = [2**x for x in range(10)]
isPowerOf2 = [True if x in powersOf2 else False for x in range(520)]

cellOffsets = [0, 1, 2, 9, 10, 11, 18, 19, 20]

indexToCell = [0]*81
cellToIndices = []

for x in range(81):
    indexToCell[x] = (x / 27) * 3 + (x % 9) / 3

for cell in range(9):
    si = 27 * (cell / 3) + 3 * (cell % 3)
    cellToIndices.append([si + x for x in cellOffsets])

affected = []
for i in range81:
    elements = set()
    rowStart = (i / 9) * 9
    colStart = i % 9
    cellIndex = indexToCell[i]

    for y in range(rowStart, rowStart+9):
        elements.add(y)

    for y in range(colStart, colStart + 80, 9):
        elements.add(y)

    for y in cellToIndices[cellIndex]:
        elements.add(y)

    elements.remove(i)
    affected.append(sorted(elements))

def display(prob):
    res = ''
    for x in range9:
        res = res + "\n" + " ".join(str(x) for x in prob[x*9: x*9 + 9])
    return res.strip()

def encode(prob):
    data = [int(x) for x in prob]
    data = [((1 << (x-1)) if x > 0 else 0) for x in data]
    return data

def decode(prob):
    from math import log
    return [int(log(x, 2) + 1.01) for x in prob]

def countOnes(num):
    count = 0
    while num > 0:
        num = num & (num - 1)
        count += 1
    return count

num2Ones = [countOnes(num) for num in range(520)]

def calcPossb(prob):
    digits = 511
    rows, cols, cells = [[0]*9 for x in range(3)]
    for row in range9:
        rv = 0
        for col in range9:
            rv |= prob[row*9 + col]
        rows[row] = rv

    for col in range9:
        cv = 0
        for row in range9:
            cv |= prob[row*9 + col]
        cols[col] = cv

    for cell in range9:
        si = 27 * (cell / 3) + 3 * (cell % 3)
        cv = 0
        for off in cellOffsets:
            cv |= prob[si + off]
        cells[cell] = cv

    psblts = [0]*81
    for x in range(81):
        if prob[x] > 0:
            continue
        row = x / 9
        col = x % 9
        cell = indexToCell[x]

        psblts[x] = digits ^ (rows[row] | cols[col] | cells[cell])
    return rows, cols, cells, psblts

def updatePsblts(prob, psblts, i, y):
    y = ~y

    for x in affected[i]:
        psblts[x] &= y
        if (prob[x] | psblts[x]) == 0:
            return False
    return True

def updatePsblts2(prob, psblts, i, y, isPowerOf2=isPowerOf2):
    y = ~y
    toSolve = []

    for x in affected[i]:
        psblts[x] &= y
        val = psblts[x]
        if isPowerOf2[val]:
            toSolve.append((x, val))
        elif (prob[x] | val) == 0:
            return False, toSolve
    return True, toSolve

def solveSimples(prob, psblts, isPowerOf2=isPowerOf2):
    toSolve = [(i, x) for i, x in enumerate(psblts) if isPowerOf2[x]]
    while toSolve:
        i, x = toSolve.pop()
        prob[i] = x
        psblts[i] = 0
        res, ts = updatePsblts2(prob, psblts, i, x)
        if not res:
            return False
        toSolve.extend(ts)
    return True

def getMinPSquare(psblts, num2Ones=num2Ones):
    loc, val = -1, 99
    for i, x in enumerate(psblts):
        xv = num2Ones[x]
        if xv == 2:
            return i, psblts[i]
        if x > 0 and xv < val:
            val = xv
            loc = i
    return loc, (psblts[loc] if loc >= 0 else None)


def solve(prob):
    # encode problem
    prob = encode(prob)
    # calc possibilities
    rows, cols, cells, psblts = calcPossb(prob)
    moves = []
    # start the loop
    while True:
        # solve simples
        if not solveSimples(prob, psblts):
            # if broken, undo last guess and make new guess
            while True:
                if len(moves) == 0:
                    # no last moves to undo
                    return False, None
                # undo last move
                nprob, npsblts, x, guesses = moves[-1]
                if guesses == 0:
                    # no more moves for this spot, move further back
                    moves.pop()
                    continue

                # take new guess
                newGuesses = (guesses & (guesses - 1))
                guess = guesses ^ newGuesses
                moves[-1][-1] = newGuesses
                prob, psblts = nprob[:], npsblts[:]
                prob[x] = guess
                psblts[x] = 0
                if updatePsblts(prob, psblts, x, guess):
                    break
        else:
            # get square with min number of psblts
            x, val = getMinPSquare(psblts)

            if x == -1:
                # if done, return "Hooray"
                return True, prob

            # make a new guess, update moves and update possibilities
            guesses = val
            newGuesses = (guesses & (guesses - 1))
            guess = guesses ^ newGuesses
            moves.append([prob[:], psblts[:], x, newGuesses])
            prob[x] = guess
            psblts[x] = 0
            if updatePsblts(prob, psblts, x, guess):
                continue
            # the last guess did not work out... make further guesses
            while True:
                if len(moves) == 0:
                    # no last moves to undo
                    return False, None
                # undo last move
                nprob, npsblts, x, guesses = moves[-1]
                if guesses == 0:
                    # no more moves for this spot, move further back
                    moves.pop()
                    continue

                # take new guess
                newGuesses = (guesses & (guesses - 1))
                guess = guesses ^ newGuesses
                moves[-1][-1] = newGuesses
                prob, psblts = nprob[:], npsblts[:]
                prob[x] = guess
                psblts[x] = 0
                if updatePsblts(prob, psblts, x, guess):
                    break


totalTime = 0

for ptype in ['easy', 'medium', 'hard']:
    ttm = []
    for ix, (pr, sol) in enumerate(problems[ptype].items()):
        st = time()
        res, prob = solve(pr)
        et = time()
        assert decode(prob) == [int(x) for x in sol]
        ttm.append(et - st)
        if res:
            print 'Solved %s #%s in %10.6f seconds' % (ptype, ix, et - st)
        else:
            print 'FAIL: %s #%s' % (ptype, ix)
    print 'Time for %s: %s' % (ptype, sum(ttm))
    totalTime += sum(ttm)

print 'Total time: %s' % totalTime
