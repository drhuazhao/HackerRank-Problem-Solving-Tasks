#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    
    sum_results =[]
    remain_list =[]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            
            sum = keyboards[i] + drives[j]
            sum_results.append(sum)
    
    sum_result_list = sorted(sum_results)[::-1]
    print(sum_result_list)
            
    for i in sum_result_list:
        if i >b:
            pass
        else:
            remain_list.append(i)
    if remain_list:
        result = (max(remain_list))
    else:
        result = -1
    
    return (result)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

