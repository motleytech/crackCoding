import numpy as np
from scipy.optimize import least_squares
from curve_fit_models import models, algos
import timeit

xdata = np.array([x*100 for x in range(1, 17)])

inputs = [
    [100*x for x in range(1, 10)],  # O(1)
    [int(10*pow(x, 1.5)) for x in range(1, 20)],  # O(log(n))
    [1000*x for x in range(1, 20)], # O(sqrt(n))
    [100*x for x in range(1, 20)],  # O(n)
    [100*x for x in range(1, 20)],  # O(n log n)
    [50*x for x in range(1, 20)],   # O(n sqrt(n))
    [20*x for x in range(1, 12)],   # O(n^2)
    [20*x for x in range(1, 12)],   # O(n^2 log(n))
    [10*x for x in range(1, 12)],   # O(n^2 sqrt(n))
    [x for x in range(3, 12)],   # O(2^n)
]

numRuns = 10
for idx, algo in enumerate(algos):
    runTimeData = []
    for size in inputs[idx]:
        runTest = lambda : algo(size)
        __builtins__._funcBeingEstimated_ = runTest
        runTime = timeit.timeit("_funcBeingEstimated_()", number=numRuns)
        runTimeData.append(runTime)

    for model, func, jac, numParams in models:
        ydata = np.array(runTimeData)
        xdata = np.array(inputs[idx])

        t_init = np.array([0.01]*numParams)

        res = least_squares(func, t_init, jac=jac, bounds=(-100, 100),
         args=(xdata, ydata), verbose=1)
        if res.cost < 0.001:
            print "%s : %s : %s" % (idx, numParams, res.cost)
            break
