#!/usr/bin/python

# 10.223.157.186 - - [15/Jul/2009:15:50:51 -0700] "GET /assets/css/960.css HTTP/1.1" 304 -

import sys

oldIp = None
totalHits = 0

for line in sys.stdin:
	data = line.strip().split('\t')
	if len(data) != 2:
		continue

	thisIp, thisHit = data

	if oldIp and oldIp != thisIp:
		print('{0}\t{1}'.format(oldIp,totalHits))
		oldIp = thisIp
		totalHits = 0

	oldIp = thisIp
	totalHits += 1

if oldIp != None:
	print('{0}\t{1}'.format(oldIp,totalHits))
