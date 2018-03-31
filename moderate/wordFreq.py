'''
count the freq of a given work in a book
'''

import string
from collections import defaultdict
from pprint import pprint as pp

freq = defaultdict(lambda : 0)

def cleanBook(book):
    'clean the book data. convert to lowercase, remove punctuation, etc'
    book = book.lower()
    chars = set(book)

    wordChars = string.ascii_lowercase + ' \n'
    toRemove = set()

    for ch in chars:
        if ch not in wordChars:
            toRemove.add(ch)

    for ch in toRemove:
        book = book.replace(ch, '')

    while '  ' in book:
        book = book.replace('  ', ' ')

    return book

def findAllFreq(book):
    'find freq of all words... this can be used later to find freq of any word'
    lines = book.split('\n')
    for line in lines:
        for word in line.split(' '):
            if len(word) > 0:
                freq[word] += 1
    return freq

def main():
    'find the print freq of all words'
    book = open('book.txt').read()
    book = cleanBook(book)

    wfreq = findAllFreq(book)

    pp(sorted((v, k) for k, v in wfreq.items()))

if __name__ == '__main__':
    main()


