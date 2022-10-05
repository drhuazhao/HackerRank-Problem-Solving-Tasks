#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):

    # Write your code here
    
    dictionary ={}
    list_duplicate_number = ([item for item, count in collections.Counter(a).items() if count > 1])
    
    for i in range(len(a)):
         if a[i] in list_duplicate_number:
          
            
            if a[i] in dictionary.keys():
                
                dictionary[a[i]] = abs(dictionary[a[i]] - i)
                
                
            else:
                dictionary[a[i]] =i
                
    if ((dictionary.values())):
             
         result = (min(dictionary.values()))
    else:
        result =-1
    return(result)
    
    
            
            
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()

