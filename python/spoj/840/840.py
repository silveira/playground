#!/usr/bin/env python

if __name__ == "__main__":
	n = None
	tests = 0
	while(n!=0):
		n = int(raw_input())
		if(n==0):
			break
		tests +=1
		print 'Teste %d' % tests
		delta = 0
		for i in xrange(n):
			a, b = map(int, raw_input().split())
			delta += a-b
			print delta
		print
