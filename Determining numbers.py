from collections import Counter
num=int(input())
l=Counter(list(map(int,input().split())))
li=[]
for key,value in l.items():
    if(value==1): li.append(key)
li.sort()
print(*li)