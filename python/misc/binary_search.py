#!/usr/bin/env python

from random import randint

def binary_search(array, key, low, high):
    if(low>high):
        return None

    mid = (low+high)/2

    if array[mid]==key:
        return mid
    elif array[mid]>key:
        return binary_search(array, key, low, mid-1)
    else: # array[mid]<key:
        return binary_search(array, key, mid+1, high)

if __name__ == '__main__':
    l = [randint(0,100) for i in range(10)]
    l.sort()
    k = randint(0,100)
    print l, k
    print binary_search(l, k, 0, len(l))

