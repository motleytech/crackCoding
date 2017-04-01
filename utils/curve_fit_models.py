# pylint: disable=C0111, W0613
import numpy as np


def create_function_from_model(model):
    def func(t, x, y):
        return model(t, x) - y
    return func

#####################
#
# f(x, t) = t0
#
#####################

def model0(t, x):
    return t[0]

func0 = create_function_from_model(model0)

def jac0(t, x, y):
    J = np.empty((x.size, t.size))
    J[:, 0] = 1
    return J

def algo0(size):
    # this should be a constant time algorithm
    # as it has nothing to do with the input data
    dummy = []
    for x in range(100):
        for y in range(20):
            dummy.append((x, y))
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x)
#
#####################

def model1(t, x):
    return t[0] + t[1] * np.log2(x)

func1 = create_function_from_model(model1)

def jac1(t, x, y):
    J = np.empty((x.size, t.size))
    J[:, 0] = 1
    J[:, 1] = np.log2(x)
    return J

def algo1(size):
    # we need a log(n) algo
    # we will create a loop that loops log(n) times!!
    # we could muck about with binary search, but then, that's log(n) in the worst case
    # sure the average case is also almost log(n), but we would like a little cleaner data
    from math import log
    n = int(log(size, 2))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x)
#
#####################

def model2(t, x):
    return t[0] + t[1] * np.log2(x) + t[2] * np.sqrt(x)

func2 = create_function_from_model(model2)

def jac2(t, x, y):
    J = np.empty((x.size, t.size))
    J[:, 0] = 1
    J[:, 1] = np.log2(x)
    J[:, 2] = np.sqrt(x)
    return J

def algo2(size):
    # we need a O(sqrt(n)) algo
    import math
    n = int(math.sqrt(size))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x
#
#####################

def model3(t, x):
    return t[0] + t[1] * np.log2(x) + t[2] * np.sqrt(x) + t[3] * x

func3 = create_function_from_model(model3)

def jac3(t, x, y):
    J = np.empty((x.size, t.size))
    J[:, 0] = 1
    J[:, 1] = np.log2(x)
    J[:, 2] = np.sqrt(x)
    J[:, 3] = x
    return J

def algo3(size):
    # we need a O(n) algo
    n = size
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x + t4 * x * log2(x)
#
#####################

def model4(t, x):
    lgx = np.log2(x)
    return t[0] + t[1] * lgx + t[2] * np.sqrt(x) + \
        t[3] * x + t[4] * x * lgx

func4 = create_function_from_model(model4)

def jac4(t, x, y):
    J = np.empty((x.size, t.size))
    lgx = np.log2(x)
    J[:, 0] = 1
    J[:, 1] = lgx
    J[:, 2] = np.sqrt(x)
    J[:, 3] = x
    J[:, 4] = x * lgx
    return J

def algo4(size):
    # we need a O(n log n) algo
    import math
    n = int(size * math.log(size, 2))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x + t4 * x * log2(x) + t5 * x * sqrt(x)
#
#####################

def model5(t, x):
    sqx = np.sqrt(x)
    lgx = np.log2(x)
    return t[0] + t[1] * lgx + t[2] * sqx + \
        t[3] * x + t[4] * x * lgx + t[5] * x * sqx

func5 = create_function_from_model(model5)

def jac5(t, x, y):
    J = np.empty((x.size, t.size))
    lgx = np.log2(x)
    sqx = np.sqrt(x)
    J[:, 0] = 1
    J[:, 1] = lgx
    J[:, 2] = sqx
    J[:, 3] = x
    J[:, 4] = x * lgx
    J[:, 5] = x * sqx
    return J

def algo5(size):
    # we need a O(n sqrt(n)) algo
    import math
    n = int(size * math.sqrt(size))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x + t4 * x * log2(x) + t5 * x * sqrt(x) \
#          + t6 * x * x
#
#####################

def model6(t, x):
    sqx = np.sqrt(x)
    lgx = np.log2(x)
    return t[0] + t[1] * lgx + t[2] * sqx + \
        t[3] * x + t[4] * x * lgx + t[5] * x * sqx + \
        t[6] * x * x

func6 = create_function_from_model(model6)

def jac6(t, x, y):
    J = np.empty((x.size, t.size))
    lgx = np.log2(x)
    sqx = np.sqrt(x)
    J[:, 0] = 1
    J[:, 1] = lgx
    J[:, 2] = sqx
    J[:, 3] = x
    J[:, 4] = x * lgx
    J[:, 5] = x * sqx
    J[:, 6] = x * x
    return J

def algo6(size):
    # we need a O(n^2) algo
    n = size * size
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x + t4 * x * log2(x) + t5 * x * sqrt(x) \
#          + t6 * x * x + t7 * x * x * log2(x)
#
#####################

def model7(t, x):
    sqx = np.sqrt(x)
    lgx = np.log2(x)
    xx = x * x
    return t[0] + t[1] * lgx + t[2] * sqx + \
        t[3] * x + t[4] * x * lgx + t[5] * x * sqx + \
        t[6] * xx + t[7] * xx * lgx

func7 = create_function_from_model(model7)

def jac7(t, x, y):
    J = np.empty((x.size, t.size))
    lgx = np.log2(x)
    sqx = np.sqrt(x)
    xx = x * x
    J[:, 0] = 1
    J[:, 1] = lgx
    J[:, 2] = sqx
    J[:, 3] = x
    J[:, 4] = x * lgx
    J[:, 5] = x * sqx
    J[:, 6] = xx
    J[:, 7] = xx * lgx
    return J

def algo7(size):
    # we need a O(n^2 log(n)) algo
    import math
    n = int(size * size * math.log(size, 2))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x + t4 * x * log2(x) + t5 * x * sqrt(x) \
#          + t6 * x * x + t7 * x * x * log2(x) + t8 * x * x * sqrt(x)
#
#####################

def model8(t, x):
    sqx = np.sqrt(x)
    lgx = np.log2(x)
    xx = x * x
    return t[0] + t[1] * lgx + t[2] * sqx + \
        t[3] * x + t[4] * x * lgx + t[5] * x * sqx + \
        t[6] * xx + t[7] * xx * lgx + t[8] * xx * sqx

func8 = create_function_from_model(model8)

def jac8(t, x, y):
    J = np.empty((x.size, t.size))
    lgx = np.log2(x)
    sqx = np.sqrt(x)
    xx = x * x
    J[:, 0] = 1
    J[:, 1] = lgx
    J[:, 2] = sqx
    J[:, 3] = x
    J[:, 4] = x * lgx
    J[:, 5] = x * sqx
    J[:, 6] = xx
    J[:, 7] = xx * lgx
    J[:, 8] = xx * sqx
    return J

def algo8(size):
    # we need a O(n^2 sqrt(n)) algo
    import math
    n = int(size * size * math.sqrt(size))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


#####################
#
# f(x, t) = t0 + t1 * log2(x) + t2 * sqrt(x) \
#          + t3 * x + t4 * x * log2(x) + t5 * x * sqrt(x) \
#          + t6 * x * x + t7 * x * x * log2(x) + t8 * x * x * sqrt(x) \
#          + t9 * 2 ^ (t10 * x)
#
#####################

def model10(t, x):
    sqx = np.sqrt(x)
    lgx = np.log2(x)
    xx = x * x
    return t[0] + t[1] * lgx + t[2] * sqx + \
        t[3] * x + t[4] * x * lgx + t[5] * x * sqx + \
        t[6] * xx + t[7] * xx * lgx + t[8] * xx * sqx + \
        t[9] * np.exp(t[10] * x)

func10 = create_function_from_model(model10)

def jac10(t, x, y):
    J = np.empty((x.size, t.size))
    lgx = np.log2(x)
    sqx = np.sqrt(x)
    xx = x * x
    xxp = np.exp(t[10] * x)
    J[:, 0] = 1
    J[:, 1] = lgx
    J[:, 2] = sqx
    J[:, 3] = x
    J[:, 4] = x * lgx
    J[:, 5] = x * sqx
    J[:, 6] = xx
    J[:, 7] = xx * lgx
    J[:, 8] = xx * sqx
    J[:, 9] = xxp
    J[:, 10] = t[9] * x * xxp
    return J

def algo10(size):
    # we need a O(e^n) algo
    import math
    n = int(math.exp(size))
    result = 0
    for x in range(n):
        for y in range(100):
            result = y + x
    return None


models = [
    (model0, func0, jac0, 1),
    (model1, func1, jac1, 2),
    (model2, func2, jac2, 3),
    (model3, func3, jac3, 4),
    (model4, func4, jac4, 5),
    (model5, func5, jac5, 6),
    (model6, func6, jac6, 7),
    (model7, func7, jac7, 8),
    (model8, func8, jac8, 9),
    (model10, func10, jac10, 11)
]

algos = [
    algo0,
    algo1,
    algo2,
    algo3,
    algo4,
    algo5,
    algo6,
    algo7,
    algo8,
    algo10,
]
