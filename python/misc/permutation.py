#!/usr/bin/env python
# inspired by the algorithm presented in the book Computer Algorithms by Horowitz, Sahni and Rajasekeran.

def perm(a,k=0):
	if(k==len(a)):
		print a
	else:
		for i in xrange(k,len(a)):
			a[k],a[i] = a[i],a[k]
			perm(a, k+1)
			a[k],a[i] = a[i],a[k]



perm([1,2,3])
