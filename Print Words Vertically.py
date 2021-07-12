n=input()
l=n.split(" ")
maxi=0
for i in l:
    if(len(i)>maxi): maxi=len(i)
word=[]
for i in l:
    if(len(i)<maxi):
        i+=(maxi-len(i))*"*"
        word.append(i)
    else: word.append(i)
s=""
li=[]
for i in range(maxi):
    for j in word:
        li=list(j)
        s+=li[i]
    s+=" "
print((s.strip()).strip("*"))