#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    
    bill_f =0
    
    for i in range(len(bill)):
        if i == k:
            pass
        else:
            bill_f= bill[i] + bill_f
   
    
    each_s_pay = int(bill_f/2)
    
    
    if each_s_pay == b:
        r = "Bon Appetit"
        
    else:
        r = (b - each_s_pay)
        
    return(r)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
