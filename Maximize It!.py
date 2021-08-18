from itertools import product
num=input().split()
l=[]
for i in range(int(num[0])):
    s=list(map(int,input().split()))
    l.append(s[1:])
max,sum=0,0
for i  in list(product(*l)):
    for j in i:
        mult=j*j
        sum+=mult
    if(sum%int(num[1])>max):
        max=sum%int(num[1])
    sum=0
print(max)