#!/usr/bin/python
"""
Post and Answer Length

We are interested to see if there is a correlation between the length of a post and the length of answers.

Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer
(just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get
the required result.
"""

'''
process forum_node data
'''

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) != 19:
            continue
        
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id,\
        last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
        
        # if the post is question, save in the question type
        if node_type == 'question':
            writer.writerow([id, "Q",len(body)])
        elif node_type == 'answer':
            writer.writerow([abs_parent_id,"A",len(body)])
            
if __name__ == "__main__":
    mapper()
