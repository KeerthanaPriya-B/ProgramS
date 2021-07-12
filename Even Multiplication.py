n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
mul,flag=1,0
for i in l:
    if(i%2==0):
        mul*=i
        flag=1
if(flag==1):
    print(mul)
else: print("0")