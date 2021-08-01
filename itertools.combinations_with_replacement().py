from itertools import combinations_with_replacement
strr=input().split()
a=list(combinations_with_replacement(sorted(strr[0]),int(strr[1])))
for i in a:
    for j in i:
        print(j,end='')
    print()