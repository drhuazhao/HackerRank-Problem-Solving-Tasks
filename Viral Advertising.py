#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    
    result =0
    day1People_number = 5
    for i in range(n):
        if i ==0: #first day
            halfNext= int(day1People_number/2)
           
            result = halfNext+ result
        else: #days after the first day
            shareFriends = halfNext*3
            
            halfNext = int(shareFriends/2)
            
            result = halfNext+ result


    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

