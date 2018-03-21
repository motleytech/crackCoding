'''
Attempts to measure the average time for a context switch
 - only works on a single processor system.

In a multiprocessor system, the 2 processes could run concurrently on
separate processes wihtout any context switch actually taking place.
'''

import os
import time

def readAndWritePipe(rp, wp):
    'read from rp and write to wp'
    os.read(rp, 5)
    os.write(wp, 'abcde')

def writeAndReadPipe(rp, wp):
    'write to wp and read from rp'
    os.write(wp, 'abcde')
    os.read(rp, 5)

def main():
    '''creates 2 pipes, forks the process and alternatively reads and
    writes from the pipes in the parent and child process'''

    rp1, wp1 = os.pipe()
    rp2, wp2 = os.pipe()
    pid = os.fork()

    numSwitches = 100
    count = numSwitches

    if pid:
        # parent
        contextSwitchTimes = []
        while count > 0:
            st1 = time.time()
            readAndWritePipe(rp1, wp2)
            contextSwitchTimes.append(time.time() - st1)
            count -= 1
        print 'average parent switch times: %s' % (sum(contextSwitchTimes) / (2 * numSwitches))

    else:
        # child
        contextSwitchTimes = []
        while count > 0:
            st2 = time.time()
            writeAndReadPipe(rp2, wp1)
            contextSwitchTimes.append(time.time() - st2)
            count -= 1
        print 'average child switch times: %s' % (sum(contextSwitchTimes) / (2 * numSwitches))


if __name__ == '__main__':
    main()
