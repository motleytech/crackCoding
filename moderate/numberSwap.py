'''
Swap 2 numbers in place
'''

def swapNumsAdd(nums):
    'swap using add / subtract. Overflow could be a problem in C / Java'
    nums[1] += nums[0]
    nums[0] = nums[1] - nums[0]
    nums[1] = nums[1] - nums[0]
    return nums


def swapNumsXor(nums):
    'swap using XOR operator.'
    nums[1] ^= nums[0]
    nums[0] = nums[1] ^ nums[0]
    nums[1] = nums[1] ^ nums[0]
    return nums


def test():
    assert swapNumsAdd([2, 3]) == [3,2]
    assert swapNumsXor([2, 3]) == [3,2]
    print 'done'

if __name__ == '__main__':
    test()
