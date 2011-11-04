#!/usr/bin/env python

if __name__ == "__main__":
	n = None
	tests = 0
	while(n!=0):
		n = int(raw_input())
		if(n==0):
			break
		player_a = raw_input()
		player_b = raw_input()
		tests +=1
		print 'Teste %d' % tests
		for i in xrange(n):
			a, b = map(int, raw_input().split())
			if((a+b) % 2 == 0):
				print player_a
			else:
				print player_b
		print
	
