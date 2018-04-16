#!/usr/bin/python

import sys
import csv
import re
import operator

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    preTag = None
    tagCounts = 0
    tag_count_pair = []
    
    for line in reader:
        if len(line) != 2:
            continue
        
        thisTag, quesCounts = line
        
        if preTag and preTag != thisTag:
            tag_count_pair.append([tagCounts, preTag])
            tagCounts = 0
    
        tagCounts += int(quesCounts)
        preTag = thisTag
        
    if preTag != None:
        tag_count_pair.append([tagCounts, preTag])
        
    sortCounts = sorted(tag_count_pairs, key = lambda x: x[0], reverse=True)
    
    for counts, tag in sortCounts[:10]:
        writer.writerow([tag, counts])
        
    """
    preTag = None
    tagCounts = 0
    tag_count_pair = []
    
    for line in reader:
        if len(line) != 2:
            continue
        
        thisTag, quesCounts = line
        
        if preTag and preTag != thisTag:
            if len(tag_count_pair) < 10:
                tag_count_pair.append([tagCounts, preTag])
            else:
                minPairCounts = min(tag_count_pairs)[0]
                if tagCounts > minPairCounts:
                    tag_count_pair[tag_count_pair.index(min(tag_count_pairs))] = [tagCounts, preTag]
            tagCounts = 0
    
        tagCounts += int(quesCounts)
        preTag = thisTag
        
    if preTag != None:
         if len(tag_count_pair) < 10:
                tag_count_pair.append([tagCounts, preTag])
            else:
                minPairCounts = min(tag_count_pairs)[0]
                if tagCounts > minPairCounts:
                    tag_count_pair[tag_count_pair.index(min(tag_count_pairs))] = [tagCounts, preTag]
    
    for counts, tag in tag_count_pair:
        writer.writerow([tag, counts])
    """


"""
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    preTag = None
    # counts = 0
    tag_counts = {}
    tags = {}
    
    for line in reader:
        if len(line) != 2:
            continue
        
        thisTag, thisQuestion = line
        
        if not tags.has_key(thisTag):
            tags[thisTag] = []
            tag_counts[thisTag] = 0
            
        tag_counts[thisTag] += 1
        tags[thisTag].append(thisQuestion)
        
    top_N_tags = sorted(tag_counts.items(),key=operator.itemgetter(1),reverse=True)[:10]
    
    for (tag, count) in top_N_tags:
        writer.writerow([tag,count])
        # print('{0}\t{1}'.format(tag,count))
        # writer.writerow([tag,','.join(tags)])
"""

if __name__ == "__main__":
    reducer()
