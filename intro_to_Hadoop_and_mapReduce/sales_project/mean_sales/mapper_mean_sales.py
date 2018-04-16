#!/usr/bin/python

# Write a mapreduce program that processes the purchases.txt file and outputs mean (average) of sales for each weekday.
# To get the weekday, use this expression: weekday = datetime.strptime(date, "%Y-%m-%d").weekday()

import sys
from datetime import datetime

def mapper():
	for line in sys.stdin:
		data = line.split('\t')
		if len(data) == 6:
			date, time, store, item, cost, payment = data
			weekday = datetime.strptime(date, '%Y-%m-%d').weekday() # output is number
			print('{0}\t{1}'.format(weekday, cost)

if __name__ == "__main__":
	mapper()
