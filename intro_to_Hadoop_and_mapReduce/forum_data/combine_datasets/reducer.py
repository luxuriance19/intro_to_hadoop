#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

"""
import sys

def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t',quotechar='"',quoting=csv.QUOTE_ALL)
    key_Node = None
    key_User = None
    for line in sys.stdin:
        data = line.strip().split()
        if data[1] == "Node":
            key_Node = data[0]
            data_Node = data[2:] #length = 8
        elif data[1] == 'User': 
            key_User = data[0]
            data_User = data[2:] # length=4
            
        if key_Node == key_User:
            writer.writerow(data_Node[:3]+key_User+data_Node[3:]+data_User)
        # YOUR CODE HERE
"""      
import sys
import csv
def reducer():
    reader = csv.reader(sys.stdin,delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',quotechar = '"', quoting=csv.QUOTE_ALL)
    
    preUser = None
    thisUser = None
    
    id = title = tagnames = author_id = node_type = parent_id = abs_parent_id = added_at = score = reputation \
    = gold = silver = bronze = ""
    source = None
    
    for line in reader:
        if len(line) == 10:
            thisUser,source,id,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score = line
        elif len(line) == 6:
            thisUser,source,reputation, gold, silver, bronze = line
            
        if preUser and thisUser!=preUser:
            writer.writerow([id,title,tagnames,preUser, node_type, parent_id, abs_parent_id, added_at,\
            score, reputation, gold, silver, bronze])
            
        preUser = thisUser
    
    if preUser != None:
        writer.writerow([id, title, tagnames, prevUser, node_type, parent_id, abs_parent_id, added_at,\ 
        score, reputation, gold, silver, bronze])
        
if __name__ == "__main__":
    reducer()
        
