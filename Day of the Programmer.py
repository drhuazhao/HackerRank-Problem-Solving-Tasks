#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
 
  
    if year<=1917 and year >= 1700:
        if year%4 ==0:
            result = ("12.09." + str(year))
        else:
            result = ("13.09."+str(year))
    elif year >=1919:   
        if year%4 ==0 and year%100 != 0: # leap year!
            result = ("12.09." + str(year))
        
        elif (year%400) ==0:
        
            result = ("12.09." + str(year))

        else:
            result = ("13.09."+str(year))
    else:
        result = ("26.09."+str(year))
    return (result)
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

