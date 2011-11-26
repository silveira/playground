#!/usr/bin/env python
"""
gwu_cs_course_graph converts a csv file into a file written in dot, a graph representation language
data scraped from http://www.gwu.edu/~bulletin/grad/csci.html
spreadsheet at https://docs.google.com/spreadsheet/ccc?key=0AtuUxRrpmLaQdG5pcnNQYmhzbzdoMUZuZWZPUlQ0OVE
"""
__author__ = "Silveira Neto"
__license__ = "GPL"

import csv

# read the csv file and convert in a array of dictionaries
# TODO: use csv.DictReader
reader = csv.reader(open("GRAD CSCI - GRAD.csv","rb"))
fields = reader.next()
courses = []
for row in reader:
	items = zip(fields,row)
	item = {}
	for (name,value) in items:
			item[name] = value.strip()
	courses.append(item)


# Convert this structure into a dot file.
# First the labels and so the dependencies.
print "digraph G {"

for course in courses:
	print "\t%s [label=\"%s (%s)\"];" % (course['ID'], course['Course'], course['ID'])

for course in courses:
	if(course.has_key('Prerequisite')):
		prereqs = map(int, course['Prerequisite'].split(',')) # '6232, 6233' to [6232, 6233]
		for req in prereqs:
			print "\t%s -> %s;" % (req, course['ID'])

print "}"
