from itertools import groupby
strr=input()
for i,j in groupby(strr):
    cou=len(list(j))
    print(tuple([cou,int(i)]),end=' ')