#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    
    dict_fre ={}
    max_fre_v = []
    
    for i in range(len(arr)):
       
        if arr[i] in dict_fre.keys():
            dict_fre[arr[i]] = dict_fre[arr[i]]+ 1
        else:
            dict_fre[arr[i]] = 1
    
    max_fre = max(dict_fre.values())
    
    for i,v in dict_fre.items():
        if v == max_fre:
            
            max_fre_v.append(i)
            
 
    result = (min(max_fre_v))
    return(result)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

