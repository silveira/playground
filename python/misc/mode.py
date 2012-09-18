#!/usr/bin/env python

def mode(array):
    copy = array[:]
    copy.sort()
    
    print copy
    
    last = None
    counter = 0
    best_counter = 0
    best = None
    
    for i in copy:
        if i == last:
            counter += 1
            if(counter>best_counter):
                best = i
                best_counter = counter
        else:
            counter = 0
        last = i

    return best

if __name__=="__main__":
    print mode([1,4,6,2,4,3,1,4,5,4,4,4,8,1,1,3,1,9,5,503,1,1,24,6])