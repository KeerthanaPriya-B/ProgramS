from itertools import product
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
l=[]
l.append(a1)
l.append(a2)
print(*list(product(*l)))