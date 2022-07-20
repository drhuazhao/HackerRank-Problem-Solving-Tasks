#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
        
    i = a[(n-1)]
    nr=0
    result_numbera ={}
    result_na = 1
    result_numberb ={}
    result_nb = 1
    result_values =[]
    
    range_num = (b[(0)] - a[(n-1)])
    
    while nr <= (range_num) and i <= b[(0)]:
        
        for k in a:
            
            if k>=i:
                if k%i ==0:
                    if i in result_numbera.keys():
                       
                        result_numbera[i] = result_numbera[i] +1
                        
                    else:
                        result_numbera[i] = result_na 
                else:
                    pass
            else:
                
                if i%k ==0:
                   
                    if i in result_numbera.keys():
                        
                         result_numbera[i] = result_numbera[i] +1
                        
                    else:
                        result_numbera[i] = result_na 
                else:
                    pass
                
        for j in b:
            
            if j>=i:
                if j%i ==0:
                   
                    if i in result_numberb.keys():
                        result_numberb[i] = result_numberb[i] +1
                    else:
                       
                        result_numberb[i] = result_nb
                else:
                    pass
            else:
                if i%j ==0:
                    
                    if i in result_numberb.keys():
                        result_numberb[i] = result_numberb[i] +1
                    else:
                       
                        result_numberb[i] = result_nb
                    
                else:
                    pass
    
            
        i+=a[(n-1)]
        nr+=1
        
  
    for i,v in result_numbera.items():
        if i in result_numberb.keys():
            result_numberb[i] = v + result_numberb[i]
        else:
            pass
        
    for j,r in result_numberb.items():
        
        if r==(m+n):
            result_values.append(j)
            
    
    result = len(result_values)
    
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()


