from collections import Counter
s=int(input())
string=[]
for i in range(s):
    string.append(input().split())
hash=[]
for i in string:
    for j in i:
        if(j[0]=="#"): hash.append(j)
hash.sort()
a=Counter(hash).most_common(5)
for i in a:
    for j in i:
        if(str(j).startswith('#')): print(j)