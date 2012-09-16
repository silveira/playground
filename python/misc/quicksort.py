#!/usr/bin/env python

def partition(array, begin, end):
    pivot = array[begin]
    i = begin
    j = end
    while(i<j):
        while(array[i]<=pivot):
            i+=1
        while(array[j]>pivot):
            j-=1
        if(i<j):
            array[i], array[j] =array[j], array[i]
    array[begin], array[j] =array[j], array[begin]
    return j

def quicksort(array, begin, end):
    print array
    if begin < end:
        j = partition(array, begin, end)
        quicksort(array, begin, j-1)
        quicksort(array, j+1, end)

if __name__ == '__main__':
    A = [3, 8, 5, 9, 8, 7, 2, 4, 11]
    quicksort(A, 0, len(A)-1)

