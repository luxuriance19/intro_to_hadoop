#!usr/bin/python

import sys

def reducer():
preDay = None
totalSales = 0
counts = 0

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue

	thisDay, thisSale = data

	if preDay and preDay != thisDay:
		meanSale = totalSales/counts
		print('{0}\t{1}'.format(WEEKDAY[int(PreDay)],meanSale))
		preDay = thisDay
		counts = 0
		totalSales = 0

	totalSales += float(thisSale)
	counts += 1
	preDay = thisDay

if preDay != None:
	meanSale = totalSales/counts
	print('{0}\t{1}'.format(WEEKDAY[int(PreDay)],meanSale))
	


