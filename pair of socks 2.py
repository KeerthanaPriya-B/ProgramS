s=input()
co=0
cou=0
count=0
for i in range(len(s)):
    if(s[i]=="r"):
        co+=1
    if(s[i]=="g"):
        cou+=1
    if(s[i]=="b"):
        count+=1
if(co%2==0 and cou%2==0 and count%2==0):
    print("true")
else:
    print("false")
    