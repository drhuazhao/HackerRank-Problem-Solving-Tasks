#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
 
    result =[]
    for i in range(len(arr)):
        
        for j in range(1,len(arr)):
            if i ==j or j<i:
                pass
            else:
                
                
                if arr[i] + arr[j] == m:
                    
                    result.append(i+1)
                    result.append(j+1)
  
    return(result)
                    
            
    
            
        
            
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

