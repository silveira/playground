#!/usr/bin/env python

"""
Problem: merge k sorted lists of size up to n.
Solution: two approaches, functions merge_and_sort and merge_many.
"""

"""
A trivial solution, put all lists together and sort it. 
Time complexity: O(log(nk))
( without making any assumptions about how the python's sort take advantage of
pre-sorted ranges in the list )
"""
def merge_and_sort(lists):
   retlist = []
   for list in lists:
      retlist.extend(list)
   retlist.sort()
   return retlist

"""
Merge two sorted lists in a sorted list.
This function is used by the function merge_many.
Time complexity: O(len(first)+len(second))
"""
def merge_two(first, second):
   merged = []
   i = 0
   j = 0
   while i<len(first) and j<len(second):
      if first[i]==second[j]:
         merged.append(first[i])
         merged.append(second[j])
         i += 1
         j += 1
      elif first[i]>second[j]:
         merged.append(second[j])
         j += 1
      else:
         merged.append(first[i])
         i += 1
      
      if i==len(first):
         merged.extend(second[j:])
         break
         
      if j==len(second):
         merged.extend(first[i:])
         break

   return merged
   
"""
Merge sorted lists, two by two.
Time complexity: O(nlog(k))
"""
def merge_many(lists):
   queue = lists[:]
   while(len(queue)>1):
      first = queue.pop(0)
      second = queue.pop(0)
      queue.append(merge_two(first, second))
   return queue.pop(0)

if __name__ == '__main__':
   print merge_and_sort([[2,10,30,40],[9,11],[3,5,9,10]])
   print merge_many([[2,10,30,40],[9,11],[3,5,9,10]])
