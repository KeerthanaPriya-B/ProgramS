from collections import Counter 
seq = input()
flag=0
a=Counter(seq)
for i in seq:
    if i in '7890':
        print('-1')
        flag=1
        break
if flag==0: print(len(seq)-int(a['6']))