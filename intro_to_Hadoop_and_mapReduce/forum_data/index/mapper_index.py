#!usr/bin/python
import sys
import csv
import re

# WRite a Mapreduce program that creates an index of all words that can be found in the body of forum posts, and the node they were found in.
# Do not parse HTML. Split the text on all whitespace, as well as the following characters: .!?:;"()<>[]#$=~/

# Questions that should be answerable:
# How many times was the word 'fantastic' used in forums?
# List of comma separated nodes where the word fantastically can be found. List the nodes in ascending order (1,2,3,4,5...)

def mapper():
	reader = csv.reader(sys.stdin,delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"',quoting=csv.QUOTE_ALL)

	for line in reader:
		try:
			node_id = int(line[0].strip())
			body = line[4]
			words = filter(bool, [word,strip() for word in re.split('[^a-zA-Z0-9\']+',body)])
			for word in words:
				# print(word.lower()+'\t'+node_id)
				writer.writerow(word,node_id)

		except ValueError:
			continue

def mapper1():
	reader = csv.reader(sys.stdin, delimiter='\t')
	chars = '.!?:;"()<>[]#$=~/'
	trans = string.maketrans(chars, ' '*len(chars))
	for line in reader:
		if len(line) == 19:
			body = line[4]
			node_id = line[0]
			body = body.translate(trans)
			words = body.strip().split()
			for words in words:
				print(word.lower()+'\t'+node_id)
			

if __name__ == "__main__":
	mapper()

