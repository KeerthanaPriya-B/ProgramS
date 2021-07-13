import math
import os
import random
import re
import sys

def marsExploration(s):
    
  cou=0
  for i in range(len(s)):
    if (i%3==0) and (s[i]!='S') :
        cou+=1
    if (i%3==1) and (s[i]!='O') :    
        cou+=1
    if (i%3==2) and (s[i]!='S') :
        cou+=1              
  return cou 
      
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
