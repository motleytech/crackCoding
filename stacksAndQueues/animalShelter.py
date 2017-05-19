'''
implementation of the animal shelter queue
'''

from queue import Queue

class AnimalShelterQueue(object):
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.count = 0

    def enqueueDog(self, dog):
        self.dogs.push((dog, self.count))
        self.count += 1
        return self

    def enqueueCat(self, cat):
        self.cats.push((cat, self.count))
        self.count += 1
        return self

    def dequeueAny(self):
        if self.dogs.isEmpty() and self.cats.isEmpty():
            raise Exception("No animals in queue")

        if self.dogs.isEmpty():
            aqueue = self.cats
        elif self.cats.isEmpty():
            aqueue = self.dogs
        else:
            dog, dc = self.dogs.peek()
            cat, cc = self.cats.peek()
            if dc < cc:
                aqueue = self.dogs
            else:
                aqueue = self.cats
        return aqueue.pop()[0]

    def dequeueDog(self):
        if self.dogs.isEmpty():
            raise Exception("No dogs in queue")
        return self.dogs.pop()[0]

    def dequeueCat(self):
        if self.cats.isEmpty():
            raise Exception("No cats in queue")
        return self.cats.pop()[0]

def test():
    '''
    test for AnimalShelterQueue class
    '''
    asq = AnimalShelterQueue()
    (asq.enqueueCat('c1').enqueueDog('d1').enqueueDog('d2')
     .enqueueCat('c2').enqueueCat('c3').enqueueDog('d3')
     .enqueueCat('c4').enqueueCat('c5'))

    assert asq.dequeueDog() == 'd1'
    assert asq.dequeueAny() == 'c1'
    assert asq.dequeueCat() == 'c2'
    assert asq.dequeueDog() == 'd2'
    print 'test passed'


if __name__ == '__main__':
    test()
