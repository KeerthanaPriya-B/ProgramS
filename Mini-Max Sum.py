import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    x = arr[:4]
    y = sum(x)
    x1 = arr[1:]
    y1 = sum(x1)
    print(str(y)+' '+ str(y1))
    

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)
