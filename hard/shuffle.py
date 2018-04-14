'''random shuffle'''

from random import gauss

def shuffle(cards):
    'randomly shuffle the cards'
    nums = sorted([(gauss(0, 10), i) for i, x in enumerate(range(52))])
    return [cards[x[1]] for x in nums]

def test():
    'test for shuffle method'
    print shuffle(range(52))

if __name__ == '__main__':
    test()
