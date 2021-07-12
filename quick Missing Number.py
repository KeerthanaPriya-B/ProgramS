s=input()
l=[]
a=[]
for i in s.split(" "):
    l.append(i)
le=len(l)
for i in l:
    a.append(int(i))
for i in range(le+1):
    if(i not in a):
        print(i)
        