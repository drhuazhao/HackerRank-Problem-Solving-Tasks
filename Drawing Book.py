#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here

    group_pages = []
    if (n-1)%2==0:
        listgroup_Pages = (list(range(n+1)))
        print(listgroup_Pages)
        PG = 2
        sublist = [listgroup_Pages[i:PG+i] for i in range(0, n, PG)] # set pages to groups [0,1],[2,3],....,[n-1,n]
        
        for i in range(len(sublist)):
            print(sublist[i])
            if p in sublist[i]:
                #checking the first page of the book to p
                firstPage_to_p = i
                
            #checking the last page's group number
            if n in sublist[i]:
                lastPage_group_num = i

        lastPage_to_p = lastPage_group_num - firstPage_to_p
        
        #compare two distances
        if firstPage_to_p> lastPage_to_p:
            result = lastPage_to_p
        else:
            result = firstPage_to_p
            
    else:
        listgroup_pages = list(range(n+2))
        PG=2
        sublist = [listgroup_pages[i:PG+i] for i in range(0, n+2, PG)]
        print(sublist)
        
        for i in range(len(sublist)):
            if p in sublist[i]:
                #checking the first page of the book to p
                print(p,i)
                firstPage_to_p = i
            else:
                pass
                
            #checking the last page's group number
            if n in sublist[i]:
                lastPage_group_num = i
            else:
                pass
        lastPage_to_p = lastPage_group_num - firstPage_to_p
        if firstPage_to_p> lastPage_to_p:
            result = lastPage_to_p
        else:
            result = firstPage_to_p
    
    return (result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

