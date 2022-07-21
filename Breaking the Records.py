#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
   
    
    
    bestscore =scores[0]
    worstscore =scores[0]
    bestscorenum =0
    worstscorenum =0
    
    for i in range(len(scores)):
        
        
        if scores[i] > bestscore:
               bestscore = scores[i]
               
               bestscorenum = bestscorenum +1
        elif scores[i] < worstscore:
            worstscore = scores[i]
            
            worstscorenum = worstscorenum +1
            
        else:
            pass
    
    return(bestscorenum, worstscorenum)
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
