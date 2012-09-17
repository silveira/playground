#!/usr/bin/env python

def set_C(A,B):
    C = []
    i = 0
    j = 0
    
    last_A = None
    last_B = None
    
    while(i<len(A) and j<len(B)):
        if(A[i]==B[j]):            
            C.append(A[i])
            i+=1
            j+=1
        elif (A[i]>B[j]):
            j+=1
        else:
            i+=1

    return C
     
if __name__=="__main__":
    pass
    #print set_C([1,2,3,7],[3,4,5,7])
    #print set_C([3],[3])