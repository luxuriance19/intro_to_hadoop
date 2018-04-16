#!usr/bin/python

import sys

salesTotal = 0
olditem = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 2:#something has gone wrong.because mapper writing the data out in 2
		continue

	thisItem, thisSale = data
	
	if oldItem and oldItem != thisItem:
		print('{0}\t{1}'.format(oldItem,salesTotal))
		oldItem = thisItem
		salesTotal = 0
	
	salesTotal += float(thisSale)
	oldItem = thisItem

if oldItem != None:
	print('{0}\t{1}'.format(oldItem,salesTotal))

	
	
