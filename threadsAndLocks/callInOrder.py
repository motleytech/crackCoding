'''Use semaphores to sync locks across different threads'''

import threading
import time

sem1 = threading.Semaphore()
sem2 = threading.Semaphore()

result = []

def first():
    result.append('first')
    sem1.release()

def second():
    sem1.acquire()
    result.append('second')
    sem1.release()
    sem2.release()

def third():
    sem2.acquire()
    result.append('third')
    sem2.release()

def myMethod(index, method):
    method()


def main():
    sem1.acquire()
    sem2.acquire()
    threads = []
    methods = [first, second, third]
    for x in range(3):
        threads.append(threading.Thread(target=myMethod, args=(x, methods[x])))

    for th in threads:
        th.start()

    for th in threads:
        th.join()


def test():
    for x in range(3000):
        while len(result) > 0:
            result.pop()

        main()

        assert result[0] == 'first'
        assert result[1] == 'second'
        assert result[2] == 'third'
        assert len(result) == 3

if __name__ == '__main__':
    test()
    print 'done'
