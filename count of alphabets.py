from collections import Counter
s=input()
l=Counter(s)
strr,li="",[]
for i in l.elements():
    li.append(i+":"+str(l[i]))
sort=sorted(set(li))
for i in sort:
    strr+=i+','
print("{"+strr.strip(',')+"}")