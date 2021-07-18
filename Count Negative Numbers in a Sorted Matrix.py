s=input().split('#')
count=0
for i in s:
    for j in i:
        if(j=='-'):
            count+=1
print(count)