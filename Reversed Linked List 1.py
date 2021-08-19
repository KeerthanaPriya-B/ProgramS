n=int(input())
lst= list(map(int,input().split()))
sub_arr=[]
new_list=[]
for i in lst:
    if i%2==0:
        sub_arr.append(i)
    else:
        if len(sub_arr)>0:
            sub_arr.reverse()
            new_list.extend(sub_arr)
            sub_arr=[]
        new_list.append(i)
if len(sub_arr)>0:
    sub_arr.reverse()
    new_list.extend(sub_arr)
    print(*new_list)
else:
    print(*new_list)