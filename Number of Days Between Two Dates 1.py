from datetime import date
s=input()
d1=s[slice(0,10)].split('-')
d2=s[slice(11,len(s))].split('-')
t1=date(int(d1[0]),int(d1[1]),int(d1[2]))
t2=date(int(d2[0]),int(d2[1]),int(d2[2]))
t3=str(abs(t1-t2)).split(" ")
print(t3[0])