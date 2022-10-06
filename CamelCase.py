#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here

    counting_capitial_letters = 0 
    
    for i in s:
    
        if i.isupper():
            counting_capitial_letters= counting_capitial_letters+1
    total_words = counting_capitial_letters +1
    
    return(total_words)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()

