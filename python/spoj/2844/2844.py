#!/usr/bin/env python

def is_divisible_by_eleven(n):
	"""
	>>> is_divisible_by_eleven("323455693")
	True
	>>> is_divisible_by_eleven("92075018492940392140590790129423")
	False
	"""
	toogle = True
	sum_a = 0
	sum_b = 0
	while(counter < len(n)):
		if toogle:
			sum_a += int(n[counter])
		else:
			sum_b += int(n[counter])
		toogle = not toogle
	delta = sum_a-sum_b
	if delta == 0 or delta == 11 or delta == -11:
		return True
	else:
		return False

if __name__ == "__main__":
	n = None
	while(n!='0'):
		n = raw_input()
		if(n=='0'):
			break
		
		print '%s is' % n,
		if not is_divisible_by_eleven(n):
			print 'not',
		print 'a multiple of 11' 
