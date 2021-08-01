from itertools import combinations
strr=input().split()
for k in range(1,int(strr[1])+1):
    a=list(combinations(sorted(strr[0]),k))
    for i in a:
        for j in i:
            print(j,end='')
        print()