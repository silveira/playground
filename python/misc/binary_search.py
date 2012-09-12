#!/usr/bin/env python

# recursive binary search
def binary_search_r(array, key, low, high):
	if(low>high):
		return None
	mid = (low+high)/2
	if array[mid]==key:
		return mid
	elif array[mid]>key:
		return binary_search_r(array, key, low, mid-1)
	else: # array[mid]<key:
		return binary_search_r(array, key, mid+1, high)

# non-recursive binary search
def binary_search_nr(array, key):	
	low = 0
	high = len(array)
	while(low<=high):
		mid = (low+high)/2
		if array[mid]>key:
			high = mid -1
		elif array[mid]<key: 
			low = mid + 1
		else: # array[mid]==key
			return mid
	return None

if __name__ == '__main__':
	from random import randint
	l = [randint(0,100) for i in range(10)]
	l.sort()
	k = randint(0,100)
	print l, k
	print binary_search_r(l, k, 0, len(l))
	print binary_search_nr(l, k)

# Example:
# >>> 
# [4, 7, 9, 28, 35, 40, 60, 65, 65, 80] 28
# 3
