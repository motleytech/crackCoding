'''random selection of m elements from array'''

from random import gauss

def select(arr, m):
    'return m random elements from arr'
    nums = sorted([(gauss(0, 10), i) for i, x in enumerate(range(52))])
    return [arr[x[1]] for x in nums[:m]]

def test():
    'test for select method'
    print select(range(52), 5)

if __name__ == '__main__':
    test()
