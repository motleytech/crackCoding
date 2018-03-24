'''
solution for the dining philosopher's problem.

The odd numbered philosophers eat first,
then the even numbered ones.

In case there are odd numbered philosophers (so both first
and last philosopher are even numbered), then
philosopher 0 eats after the last.

This implementation uses semaphores to allocate forks.

'''

import threading
import time

numPhilosophers = 3
sems = [threading.Semaphore() for _ in range(numPhilosophers)]

def startEating(k):
    'philosopher k starts eating'
    if k % 2 == 0 and numPhilosophers > 1:
        if k != numPhilosophers - 1:
            sems[k].acquire()
        sems[(k-1) % numPhilosophers].acquire()

    print '#%s eats' % k
    sems[k].release()
    sems[(k-1) % numPhilosophers].release()

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
    for y in range(40):
        [sem.acquire() for sem in sems]
        main()
    print 'done'
