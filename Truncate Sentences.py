n  = input().split()
length=int(n[len(n)-1])
n.pop()
dict,lst,inc= {},[],1
for i in n:
    dict[i]=inc
    inc+=1
for i in dict.items():
    if int(i[1])<=length and i[0].isalpha():
        lst .append(i[0])
print(*lst)