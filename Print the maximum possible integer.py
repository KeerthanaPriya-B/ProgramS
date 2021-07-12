n=int(input())
sum,flag,n_cou=0,0,0
l=[]
for i in str(n):
    n_cou+=int(i)
for i in range(1,n):
    for j in str(i):
        sum+=int(j)   
    if(sum>n_cou):
        l.append(i)
        flag=1
    sum=0
l.sort()
if(flag==1):
    print(l[len(l)-1])
else:
    print(n)