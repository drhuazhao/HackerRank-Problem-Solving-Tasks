#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    
    count_divisors =0
    list_number = (list(map(int,str(n))))
    
    for i in list_number:
       
        if i !=0:
            if n %i ==0:
                count_divisors = count_divisors +1
        else:
                pass
   
    return(count_divisors)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

