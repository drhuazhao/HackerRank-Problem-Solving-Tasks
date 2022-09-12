#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

     e =100
     q =(0+k)%n # first jump
     
     if c[q] ==1:
        e = e-3
     else:
        e = e-1
     list_arrived_index =[]
     
     while q:
        
        if c[(q+k)%n]==1:
            e = e-3
        else:
            e = e-1
            
        q = (q+k)%n
        
        if (q+k)%n==0:
            if c[(q+k)%n]==1:
                e = e-3
            else:
                e = e-1
            break
        else:
            continue
        

    
   
     return(e)
    
         
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()

