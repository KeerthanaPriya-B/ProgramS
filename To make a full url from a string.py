s=input().split('#')
l=[]
l1=[]
for i in range(len(s)):
    if(i<3):
        l.append(s[i])
    else:
        l1.append(s[i])
first_part='.'.join(l)
second_part='/'.join(l1)
print('https://'+first_part+'/'+second_part+'/')