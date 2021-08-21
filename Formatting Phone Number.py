import re
a = ''.join(re.split(' |-',input()))
n,m,strr,lst,s,count,sec_last,last_ele,str = 0,3,'',[],'',0,'','',''
for i in range(len(a)):
    strr += a[n:m]+'-'
    s += a[n:m]
    if s not in lst: lst.append(s)
    n,m,s = m,m+3,''
n,m = 0,3
for i in range(len(a)//3):
    str += a[n:m]+'-'
    n,m = m,m+3
lst.remove('')
if len(lst[len(lst)-1]) == 1:
    for i in lst[len(lst)-2]:
        if count < 2:
            sec_last += i
            count += 1
        else: last_ele += i + lst[len(lst)-1]
    print(str[:len(str)-4] + sec_last+'-' + last_ele)
else:print(strr.rstrip('-'))
            
    