#!usr/bin/python

"""
最好不要在reducer中用一个数据结构存放大量的keys。因为hadoop已经将mapper通过key进行了排序。
有一样键值的键值对会被reducer认为是输入。当用的字典的键值不是原始的mapper的键值的时候可以使用字典
这个程序是实现统计每个用户在哪个小时的发布数量最多。
"""

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting = csv.QUOTE_ALL)
    
    preUser = None
    thisUser = None
    hour = None
    hourPosts = [0]*24
    
    for line in reader:
        if len(line) != 2:
            continue
        
        thisUser, hour = line
        
        if preUser and preUser != thisUser:
            maxPosts = max(hourPosts)
            for hour, posts in enumerate(hourPosts):
                if posts == maxPosts:
                    writer.writerow([preUser, hour])
            hourPosts = [0]*24
        
        preUser = thisUser
        hourPosts[hour] += 1
        
    if preUser != None:
        maxPosts = max(hourPosts)
            for hour, posts in enumerate(hourPosts):
                if posts == maxPosts:
                    writer.writerow([preUser, hour])
        
"""

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting = csv.QUOTE_ALL)
    
    preUser = None
    thisUser = None
    hour = None
    posts_at_hour = {}
    # hourPosts = [0]*24
    
    for line in reader:
        if len(line) == 2:
            thisUser, hour = line
            
            if not posts_at_hour.has_key(hour):
                posts_at_hour[hour] = 0
                
            posts_at_hour[hour] += 1
            
        if preUser and preUser != thisUsr:
            maxPostCounts = max(posts_at_hours.values())
            maxPostHours = [hour for hour, counts in posts_at_hour.items() if counts == maxPostCounts]
            for postHour in sorted(maxPostHours):
                writer.writerow([preUser,postHour])
            posts_at_hour = {}
        
        preUser = thisUser
    
    if preUser != None:
        maxPostCounts = max(posts_at_hours.values())
            maxPostHours = [hour for hour, counts in posts_at_hour.items() if counts == maxPostCounts]
            for postHour in sorted(maxPostHours):
                writer.writerow([preUser,postHour])
"""
                
if __name__ == "__main__":
    reducer()
        
