'''
estimate the order of the running time
of an algorithm emperically
'''
import timeit
from numpy.polynomial.polynomial import polyfit, polyval

def estimateOrder(func, inputDataFunc, sizes=None, numRuns=None):
    '''
    estimates the order of the runtime of the algorithm
    by recording runtimes for the func for different sized inputs
    and fitting a polynomial

    TODO: upgrade this method to use non-linear least squares
    so we can estimate non-polynomial orders like O(n log n) and O(2^n)
    '''
    # we should run the function for different input sizes and note
    # the average time for random inputs of those sizes
    # now, we have a table to input size vs time
    # we use curve fitting to estimate the order

    if not sizes:
        sizes = [100*pow(2, x) for x in range(8)]
    if not numRuns:
        numRuns = 1000

    runtimeData = []
    for size in sizes:
        inputData = inputDataFunc(size)
        runTest = lambda : func(inputData)
        __builtins__._funcBeingEstimated_ = runTest
        runTime = timeit.timeit("_funcBeingEstimated_()", number=numRuns)
        runtimeData.append(runTime)

    # choose fit with good enough relative error
    for order in range(1, 4):
        result = polyfit(sizes, runtimeData, order, full=True)
        coeff, valList = result
        residuals, rank, s_val, rcond = valList
        print (order, residuals)


def doit(N):
    result = 0
    for x in range(N+1):
        for y in range(N+1):
            result += y
    return result

estimateOrder(doit, lambda x: x, [10, 20, 40, 80, 160, 320, 640, 1280, 2560], 50)
