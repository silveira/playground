#!/usr/bin/env python

def is_divisible_by_eleven(n):
	"""
	>>> is_divisible_by_eleven("323455693")
	True
	>>> is_divisible_by_eleven("92075018492940392140590790129423")
	False
	"""

	toogle = True
	total = 0

	for i in n:
		inti = 0;
		if   (i=='0'):
			inti = 0
		elif (i=='1'):
			inti = 1
		elif (i=='2'):
			inti = 2
		elif (i=='3'):
			inti = 3
		elif (i=='4'):
			inti = 4
		elif (i=='5'):
			inti = 5
		elif (i=='6'):
			inti = 6
		elif (i=='7'):
			inti = 7
		elif (i=='8'):
			inti = 8
		elif (i=='9'):
			inti = 9

		if toogle:
			total += inti
		else:
			total -= inti
		toogle = not toogle

	return (total % 11 == 0)


if __name__ == "__main__":
	n = None
	while(n!="0"):
		n = raw_input()
		if(n=="0"):
			break
		
		print '%s is' % n,
		if not is_divisible_by_eleven(n):
			print 'not',
		print 'a multiple of 11' 
