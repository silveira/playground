#!/usr/bin/env python

# break a caesar cypher

c = "QEFP FP QEB CFOPQ QBUQ"
for k in xrange(27):
    print k,
    for letter in c:
      if letter != '':
        print chr(ord(letter)+k % ord('A')),
    print 
