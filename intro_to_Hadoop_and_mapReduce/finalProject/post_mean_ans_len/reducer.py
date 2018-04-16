#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    preQuestion = None
    thisQuestion = None
    QorA = None
    length = quesLen = ansCount = totalAnsLens = 0
    
    for line in reader:
        if len(line) != 3:
            continue
        
        thisQuestion, QorA, length = line
        
        if QorA == 'Q':
            quesLen = length
        elif QorA == 'A':
            totalAnsLens += int(length)
            ansCount += 1
        
        if preQuestion and preQuestion != thisQuestion:
            if ansCount > 0:
                aveAnsLen = totalAnsLens / ansCount
            else:
                aveAnsLen = 0
                
            writer.writerow([preQuestion, quesLen, aveAnsLen])
            
        preQuestion = thisQuestion
        
    if preQuestion != None:
        if ansCount > 0:
            aveAnsLen = totalAnsLens / ansCount
        else:
            aveAnsLen = 0
                
        writer.writerow([preQuestion, quesLen, aveAnsLen])
        
if __name__ == "__main__":
    reducer()
            
