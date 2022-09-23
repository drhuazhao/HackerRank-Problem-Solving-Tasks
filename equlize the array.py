#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    
    count_num =0
    duplicate_num =([k for k,v in Counter(arr).items() if v>1])
    print(duplicate_num)
    a = dict(Counter(arr))
    max_value = (max(list((a.values()))))
    for k,v in a.items():
        if v == max_value:
            max_num = k
    
    if len(duplicate_num)>0:
        for i in arr:
            if i == max_num:
                pass
            else:
                
                count_num= count_num+1
    else:
         count_num= len(arr)-1  
  
    return(count_num)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

