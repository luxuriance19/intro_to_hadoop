#!usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
    
    preNode = None
    authors = []
    
    for line in reader:
        if len(line) != 3:
            continue
        
        thisNode, nodeType, author = line
        
        if preNode and thisNode != preNode:
            writer.writerow([preNode, authors])
            authors = []
            
        authors.append(author)  # authors += [author]
        preNode = thisNode
        
    if preNode != None:
        writer.writerow([preNode, authors])
    
    """
    nodes_authors = {}
    
    for line in reader:
        if len(line) != 3:
            continue
        
        node_id, node_type, author_id = line
       
        if not nodes_authors.has_key(node_id):
            nodes_authors[node_id] = []
            
        nodes_authors[node_id].append(author_id)
        
    for node_id, authors in nodes_authors.items():
        writer.writerow([node_id, authors])
    """
        
if __name__ == "__main__":
    reducer()
