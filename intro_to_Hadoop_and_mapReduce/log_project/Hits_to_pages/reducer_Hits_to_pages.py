#!usr/bin/python

import sys

oldPage = None
totalHits = 0

for line in sys.stdin:
	data = line.strip().split('\t')

	if len(data) != 2:
		continue

	thisPage, thisHit = data

	if oldPage and oldPage != thisPage:
		print('{0}\t{1}'.format(oldPage, totalHits))
		oldpage = thispage
		totalHits = 0

	oldPage = thisPage
	totalHits += 1

if oldPage != None:
	print('{0}\t{1}'.format(oldPage, totalHits))
