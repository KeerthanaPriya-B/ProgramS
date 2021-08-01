from itertools import permutations
strr=input().split()
a=list(permutations(strr[0],int(strr[1])))
a.sort()
for p in a:
    for i in p:
        print(i,end='')
    print()