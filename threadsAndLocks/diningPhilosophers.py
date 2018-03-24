'''
solution for the dining philosopher's problem.

The odd numbered philosophers eat first,
then the even numbered ones.

In case there are odd numbered philosophers (so both first
and last philosopher are even numbered), then
philosopher 0 eats after the last.

This avoids deadlocks, and when working correctly, does not
even require the use of locks. However, the locks are
still used in this program to prove that no deadlock occurs.
'''

import threading
import time

numPhilosophers = 9
locks = [threading.Lock() for _ in range(numPhilosophers)]
eaten = [False] * numPhilosophers

def pickLeftFork(k):
    'acquire lock to pick up left fork'
    locks[k].acquire()

def pickRightFork(k):
    'acquire lock to pick up right fork'
    locks[(k-1)%numPhilosophers].acquire()

def unpickLeftFork(k):
    'release left fork'
    locks[k].release()

def unpickRightFork(k):
    'release right fork'
    locks[(k-1)%numPhilosophers].release()

def startEating(k):
    'philosopher k starts eating'
    while k%2 == 0 and (eaten[(k - 1) % numPhilosophers] == False or
                        (k < numPhilosophers - 1 and eaten[(k + 1) % numPhilosophers] == False)):
        time.sleep(0.001)

    pickLeftFork(k)
    pickRightFork(k)
    print '#%s eats' % k
    unpickLeftFork(k)
    unpickRightFork(k)
    eaten[k] = True

def main():
    'runs multiple simulations of philosophers eating'
    threads = []
    for x in range(numPhilosophers):
        threads.append(threading.Thread(target=startEating, args=(x, )))

    for th in threads:
        th.start()

    for th in threads:
        th.join()


if __name__ == '__main__':
    for y in range(1000):
        main()
    print 'done'
