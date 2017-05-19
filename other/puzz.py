from time import time

st = time()
digits = set(str(x) for x in range(1, 10))
nums = range(10000, 31623)

for x in nums:
    if len(digits.difference(set(str(x*x)))) == 0:
        print x, x*x
        break

for x in reversed(nums):
    if len(digits.difference(set(str(x*x)))) == 0:
        print x, x*x
        break

print '\nElapsed time : %10.6f' % (time() - st)
