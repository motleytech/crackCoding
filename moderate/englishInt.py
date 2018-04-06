'number to english text conversion method'

ones = [
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
]

teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

tens = [
    '',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety',
]


orders = [
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
    'quadrillion',
    'pentillion',
    'sextrillion',
    'septillion',
    'octillion',
    'bazillion',
    'gazillion',
]

def numl1000(num):
    'handles numbers below 1000'
    rv = ''
    if num >= 100:
        rv += ones[num / 100] + ' hundred'
        num = num % 100
        if num > 0:
            rv += ' and '

    if num == 0:
        rv += ''
    elif 1 <= num <= 9:
        rv += ones[num]
    elif 10 <= num <= 19:
        rv += teens[num - 10]
    elif 20 <= num <= 99:
        rv += tens[num / 10]
        num = num % 10
        if num > 0:
            rv += ' ' + ones[num]
    return rv

def num2words(num):
    'returns english sentense for given number'
    orignum = num
    if num == 0:
        return "zero"
    words = ""
    while num > 0:
        top3 = num
        order = 0
        while top3 >= 1000:
            top3 = top3 / 1000
            order += 1

        if num < 100 and orignum >= 1000:
            words += " and"
        words += " " + numl1000(top3)

        if order > 0:
            words += " " + orders[order]

        num = num % pow(1000, order)
    return words.strip()

def test():
    'test for num2words method'
    x = 100002007
    assert num2words(x) == 'one hundred million two thousand and seven'

    x = 3423
    assert num2words(x) == 'three thousand four hundred and twenty three'

    print 'done'


if __name__ == "__main__":
    test()
