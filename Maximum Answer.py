s=input().split()
level=input().split()
count,flag=0,0
for i in level:
    if(int(i)<=int(s[1])): count+=1
    else: 
        flag+=1
        if(flag==2):
             break
print(count)