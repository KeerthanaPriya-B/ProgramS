s1 = input()
    s2 = input()
    flag,first,second=0,'',''
    if len(s1)<len(s2):
        first=s1
        second=s2
    else: 
        first=s2
        second=s1
    for j in first:
        for k in second:
            if(j==k):
                print('YES')
                flag=1
            if flag==1: break
        if flag==1: break
    if flag==0 : print('NO')