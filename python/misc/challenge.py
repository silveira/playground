#!/usr/bin/env python

# break a caesar cypher

# ciphered message
c = "A QEFP FP QEB CFOPQ QBUQ XXXXX    "

# count how many letters we have in the alphabet
n = ord('Z') - ord('A')

for k in xrange(n+1):
    print k,
    for letter in c:
      if letter != ' ':
        print chr(ord('A') + ((ord(letter)+k)%n)),
      else:
        print letter,
    print 
