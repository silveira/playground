#!/usr/bin/env python

def merge(left, right):
	"""
	>>> merge([2,3,7], [1,4,5])
	[1,2,3,4,5,7]
	"""
	result = []
	i ,j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

def mergesort(array):
	"""
	>>> mergesort([3,1,4,1,5,9,2,6,5])
	[1, 1, 2, 3, 4, 5, 5, 6, 9]
	"""
	if len(array)==0 or len(array)==1:
		return array
	elif len(array)==2:
		if(array[0]>array[1]):
			return [array[1], array[0]]
		else:
			return array
	else:
		mid = len(array)/2
		left = mergesort(array[:mid])
		right = mergesort(array[mid:])
		return merge(left, right)

if __name__=="__main__":
#	print merge([2,3,7], [1,4,5])
	print mergesort([3,1,4,1,5,9,2,6,5])
