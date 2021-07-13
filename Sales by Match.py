import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar): 
    for i in range(n):
        for j in range(n):
            if(ar[i]>ar[j]):
                temp=ar[i]
                ar[i]=ar[j]
                ar[j]=temp   
    #ar.sort()
    count,j=0,0
    while(j<n-1):
        if(ar[j]==ar[j+1]):
            count+=1
            j+=1
        j+=1
    return count
               
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
