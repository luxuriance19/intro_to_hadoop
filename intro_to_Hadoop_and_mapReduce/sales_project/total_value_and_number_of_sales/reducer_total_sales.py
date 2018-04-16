#!/usr/bin/python

import sys

salesValue = 0
salesNumber = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue

	thisStore, thisSale = data
	salesValue += float(thisSale)
	salesNumber += 1

print('{0}\t{1}'.format(salesNumber,salesValue))
