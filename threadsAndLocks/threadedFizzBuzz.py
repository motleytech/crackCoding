'''
threaded implementation of fizzbuzz
'''

import threading

number = [0]

fizz1, fizz2 = [threading.Semaphore() for x in range(2)]
buzz1, buzz2 = [threading.Semaphore() for x in range(2)]
fizzbuzz1, fizzbuzz2 = [threading.Semaphore() for x in range(2)]

fizz1.acquire()
buzz1.acquire()
fizzbuzz1.acquire()
fizz2.acquire()
buzz2.acquire()
fizzbuzz2.acquire()



def div3():
    'method to handle printing fizz'
    while True:
        fizz1.acquire()
        if number[0] % 3 == 0 and number[0] % 5 != 0:
            print 'fizz'
        fizz2.release()
        if number[0] > 20:
            return


def div5():
    'method to handle printing buzz'
    while True:
        buzz1.acquire()
        if number[0] % 3 != 0 and number[0] % 5 == 0:
            print 'buzz'
        buzz2.release()
        if number[0] > 20:
            return


def div35():
    'method to handle printing fizzbuzz'
    while True:
        fizzbuzz1.acquire()
        if number[0] % 3 == 0 and number[0] % 5 == 0:
            print 'fizzbuzz'
        fizzbuzz2.release()
        if number[0] > 20:
            return

def count():
    'method to handle printing numbers'
    while True:
        if number[0] > 0:
            fizz2.acquire()
            buzz2.acquire()
            fizzbuzz2.acquire()

        number[0] += 1

        if number[0] % 3 != 0 and number[0] % 5 != 0:
            print number[0]

        fizz1.release()
        buzz1.release()
        fizzbuzz1.release()

        if number[0] > 20:
            return


def main():
    'the main method?'
    threads = []
    threads.append(threading.Thread(target=div3))
    threads.append(threading.Thread(target=div5))
    threads.append(threading.Thread(target=div35))
    threads.append(threading.Thread(target=count))


    for th in threads:
        th.start()

    for th in threads:
        th.join()

if __name__ == '__main__':
    main()
