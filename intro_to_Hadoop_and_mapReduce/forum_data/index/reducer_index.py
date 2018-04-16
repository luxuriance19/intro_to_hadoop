#!usr/bin/python

import sys

def reducer():
	preWord = None
	nodes = []
	
	for line in sys.stdin:
		data = line.strip().split('\t')
		if len(data) != 2:
			continue

		thisWord, thisNode = data

		if preWord and preWord != thisNode:
			print('{0}\t{1}\t{2}'.format(preWord,sorted(nodes),len(nodes)))
			preWord = thisWord
			nodes = []
		
		preWord = thisWord
		nodes.append(int(thisNode))
	
	if preWord != None:
		print('{0}\t{1}\t{2}'.format(preWord,sorted(nodes),len(nodes)))

if __name__ == "__main__":
	reducer()

