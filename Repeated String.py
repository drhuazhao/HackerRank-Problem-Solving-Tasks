#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    other_a =0
    
    
    #1.find out the dived times of 's'
    times = n%len(s)
   
    if times>0:
        times_remain = int(n/len(s))
       
        
    else:
        times_all = n/len(s)
    
    #2. counting the num of 'a' in 's'
    num_a = s.count('a')
    
    
    #3. counting the number of 'a' by 'n'
    
    if times==0:
        result = num_a*times_all
        
    elif times>0:
        fir_re = (times_remain)*num_a
        
        for i in range(times):
        
            if s[i] =='a':
                other_a = other_a +1
        result = fir_re+ other_a
    return(int(result))
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

