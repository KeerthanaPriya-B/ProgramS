n=input()
n1=input()
li=list(map(int,input().split()))
even,odd=0,0
for i in li:
    if(i%2==0): even+=1
    else: odd+=1
if(even<odd): print(even)
else: print(odd)
