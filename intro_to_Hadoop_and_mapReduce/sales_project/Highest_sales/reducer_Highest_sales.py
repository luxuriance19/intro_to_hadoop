#!/usr/bin/python

import sys

oldStore = None
totalSales = 0

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue
	
	thisStore, thisSale = data
	
	if oldStore and oldStore != thisStore:
		print('{0}\t{1}'.format(oldStore,totalSales))
		oldStore = thisStore
		totalSales = 0
	
	oldStore = thisStore
	totalSales += float(thisSale)

if oldStore != None:
	print('{0}\t{1}'.format(oldStore,totalSales))

