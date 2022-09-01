#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    
    index =0 
    dict_first_list ={}
    result_list =[]
    for i in range(len(p)):
        dict_first_list[p[i]] =i+1
    
    for j in range(len(dict_first_list.keys())):
        result = (p.index(dict_first_list[j+1])) +1
        result_list.append(result)
    return(result_list)   
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

