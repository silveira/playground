#!/usr/bin/env python

def hanoi(n, a, b, c):
	if(n>=1):
		hanoi(n-1, a, c, b)
		print "move top from",a,"to",b
		hanoi(n-1, c, b, a)

hanoi(5, "a", "b", "c")
