#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    

    begin = 0
    end = 3
    sos = "SOS"
    Counting =0
    
    while end <= len(s):
        list_r = (s[begin:end])
        if list_r == "SOS":
            pass
        
        else:
            for i in range(len(list_r)):
               if  (list_r[i]!=sos[i]):
                Counting = Counting+1
                
               
               
            
        begin = begin+3
        end = end+3
          
    return(Counting)
    
    
 

    

    
    
    
        
        
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

