from time import time
import gc

digits = set(range(0, 10))
fdgts = set(range(1, 10))

def word2num(word, values):
    num = 0
    for c in word:
        num = num * 10 + values[c]
    return num

def list2String(lst):
    lhs = lst[:-1]
    rhs = lst[-1]
    return "%s = %s" % (" + ".join(lhs), rhs)

def solve(equation):
    '''
    convert equation to a form suitable for input to
    the real solver
    '''
    if isinstance(equation, list):
        equation = list2String(equation)
    lhs, rhs = [x.strip() for x in equation.split('=')]
    lhs = [x.strip() for x in lhs.split('+')]
    lhsRev = [x[::-1] for x in lhs]
    rhsRev = rhs[::-1]

    if len(rhs) < max(len(x) for x in lhs):
        return False
    values = {}
    used = set()
    firsts = set(x[0] for x in (lhs + [rhs]))
    if eqnSolver(lhsRev, rhsRev, 0, 0, 0, values, used, firsts):
        lwords = [str(word2num(v, values)) for v in lhs]
        rword = str(word2num(rhs, values))
        return "%s = %s" % (" + ".join(lwords), rword)
    return "No solution"


def eqnSolver(lhs, rhs, row, col, sm, values, used, firsts):
    '''
    use bracktracking to solve the verbal arithmetic problem
    '''
    if row >= len(lhs):
        # we are looking at the rhs characters
        if col >= len(rhs):
            # if we have run out of characters, we are done
            return True
        c = rhs[col]
        if c in values:
            # if we have seen this character, make sure the
            # value matches
            cv = values[c]
            if cv != sm % 10:
                return False
            return eqnSolver(lhs, rhs, 0, col+1, sm / 10, values, used, firsts)
        else:
            # new character, so assign the sum to this
            # char, unless the sum is already taken
            sm1 = sm % 10
            if sm1 in used:
                return False
            values[c] = sm1
            used.add(sm1)
            if not eqnSolver(lhs, rhs, 0, col+1, sm / 10, values, used, firsts):
                del values[c]
                used.remove(sm1)
                return False
            return True
    else:
        # look at the lhs term at position 'row'
        rw = lhs[row]
        if col >= len(rw):
            # if we don't have enough characters
            return eqnSolver(lhs, rhs, row+1, col, sm, values, used, firsts)
        else:
            c = rw[col]
            if c in values:
                # we have seen this character before
                sm += values[c]
                return eqnSolver(lhs, rhs, row+1, col, sm, values, used, firsts)
            else:
                # new character - try different possible
                # digits in order
                nums = fdgts if c in firsts else digits
                for cv in nums.difference(used):
                    values[c] = cv
                    used.add(cv)
                    if not eqnSolver(lhs, rhs, row+1, col, sm+cv, values, used, firsts):
                        del values[c]
                        used.remove(cv)
                        continue
                    return True
                return False

test_cases = [
    ["send", "more", "money"],
    ["zeroes", "ones", "binary"],
    ["send", "a", "tad", "more", "money"],
    ["seven", "seven", "six", "twenty"],
    ["saturn", "uranus", "neptune", "pluto", "planets"],
    ["donald", "gerald", "robert"],
    ["fifty", "twenty", "nine", "one", "eighty"],
    ["forty", "ten", "ten", "sixty"],
    ["ein", "ein", "ein", "ein", "vier"],
    ["lets", "solve", "this", "little", "teaser"],
    ["eleven", "lagers", "revive", "general"],
    ["she", "will", "wash", "these", "shirts"],
    ["have", "a", "happy", "happy", "easter"],
    ["ohio", "hawaii", "kansas", "alaska", "indiana"],
    ["tonto", "andthe", "lone", "ranger"],
    ["accentuate", "concertina", "transsonic", "instructor"],
    ["apolitical", "penicillin", "pickpocket", "knickknack"],
    ["coincidence", "electrician", "accelerator"],
    ["compromise", "stretchiest", "microscopic", "homestretch"],
    ["happy", "holidays", "to", "all", "hohohoho"],
    ["aries", "leo", "libra", "pisces"],
    ["gemini", "virgo", "cancer"],
    ["see", "three", "little", "wolves"],
    ["earth", "air", "fire", "water", "nature"],
    ["dclix", "dlxvi", "mccxxv"],
    ["couple", "couple", "quartet"],
    ["fish", "n", "chips", "supper"],
    ["store", "and", "name", "brands"],
    ["this", "isa", "great", "time", "waster"],
    ["the", "dog", "got", "her", "on", "the", "hand", "again"],
    ["when", "i", "really", "want", "a", "thrill"],
    ["what", "a", "week", "at", "news", "this", "has", "been"],
    ["this", "it", "seems", "to", "me", "is", "the", "heart", "of", "the", "matter"],
    ['apperception', 'aristocratic', 'concessionaire', 'conscription',
     'inappropriate', 'incapacitate', 'inconsistent',
     'interception', 'osteoporosis', 'perspiration', 'prescription',
     'proscription', 'prosopopoeia', 'protectorate', 'protestation',
     'statistician', 'transoceanic', 'transpiration',
     'antiperspirant'],
]

def test():
    gc.disable()
    st = time()
    for tc in test_cases:
        solve(tc)
    et = time() - st
    gc.enable()

    print "elapsed time : %10.6f" % (et)
    #print "average time : %10.6f" % (et / len(test_cases))

[test() for x in range(20)]
