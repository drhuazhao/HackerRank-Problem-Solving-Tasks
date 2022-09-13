#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    q =n
    result =1
    while q>0:
       
        result = q*result
        q = q-1
    print(result)
    

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)

