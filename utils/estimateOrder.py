'''
estimate the order of the running time
of an algorithm emperically
'''
import timeit
from numpy.polynomial.polynomial import polyfit, polyval

def estimateOrder(func, inputData):
    '''
    estimates the order of the runtime of the algorithm
    by recording runtimes for the func for different sized inputs
    and fitting a polynomial

    todo: update this method to estimate O(n log n) and O(2^n)
    '''
    timeit.timeit("func()")
    runtimes = []


def doit(N):
    result = 0
    for x in range(N+1):
        for y in range(x, N+1):
            result += y
    return result

__builtins__.doit = doit
print __builtins__

result = timeit.timeit("doit(25)", number=10000)
print result
