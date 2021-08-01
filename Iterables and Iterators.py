from itertools import combinations
num=int(input())
ele=input().split()
index=int(input())
p=list(combinations(ele,index))
count=0
for i in p:
    if('a' in i): count+=1
print(count/len(p))