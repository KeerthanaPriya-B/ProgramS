from collections import Counter 
seq = input()
flag=0
a=Counter(seq)
for i in seq:
    if i in '7890':
        print('-1')
        flag=1
        break
if flag==0: print(len(seq)-int(a['6import math
import os
import random
import re
import sys
from collections import Counter,defaultdict

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count = Counter(a)
    occ = count.most_common(1)
    most_occur = occ[0][1]
    less=greater=0
    defau = defaultdict(int)
    for i in a:
        defau[i] +=1
        
    if defau[(occ[0][0])-1]:
        less = defau[(occ[0][0])-1]
    elif defau[(occ[0][0])+1]:
        greater = defau[(occ[0][0])+1]
        
    if greater>less:
        return most_occur+greater
    else:
        return most_occur+less
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
']))