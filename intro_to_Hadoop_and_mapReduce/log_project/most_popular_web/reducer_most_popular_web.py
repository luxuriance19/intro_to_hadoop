#!usr/bin/python

import sys

hits = 0
prePage = None

maxHits = 0
popPage = None

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue

	thisPage, thisHit = data

	if prePage and prePage != thisPage:
		if hits > maxHits:
			maxHits = hits
			popPage = prePage
		hits = 0
		prePage = thisPage

	prePage = thisPage
	hits += 1

if prePage != None:
	if hits > maxHits:
		maxHits = hits
		popPage = prePage

print('{0}\t{1}'.format(popPage,maxHits))
