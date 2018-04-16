#!/usr/bin/python

# combiner类似prereduction,帮助减少网络的带宽数，减少网络拥塞
import sys

totalSales = 0
numberOFSales = 0

preDay = None

averages = {}

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue
	
	thisDay, thisSale = data
	
	if preDay and thisDay != preDay:
		salesAverage = totalSales / numberOfSales
		averages[preDay] = salesAverage
		preDay = thisDay
		totalSales = 0
		numberOfSales = 0

	preDay = thisDay
	totalSales += float(thisSale)
	numberOfAverage += 1

if preDay != None:
	salesAverage = totalSales / numberOfSales
	averages[preDay] = salesAverage

for day in sorted(averages.keys()):
	print('{0}\t{1}'.format(day, averages[day]))

