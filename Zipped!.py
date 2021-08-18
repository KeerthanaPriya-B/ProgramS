n=input().split()
l,li,sum=[],[],0
for i in range(int(n[1])):
    l.append(input().split())
li=list(zip(*l))
for i in li:
    for j in i:
        sum+=float(j)
    print(sum/int(n[1]))
    sum=0