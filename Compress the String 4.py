import re
n = int(input())
for i in range(n):
    length = int(input())
    strr = input()
    conso,stri,s=0,'',''
    for i in range(1,len(strr)):
        stri+=strr[i]
    pattern = re.findall(r'a{2,}|e{2,}|i{2,}|o{2,}|u{2,}',stri)
    new_str=strr
    for i in pattern:
        update = new_str.replace(i,i[0])
        new_str = update   
    for i in range(1,len(new_str)):
        if new_str[i] not in 'aeiou': conso+=1        
        else:
            if conso!=0: s+=str(conso)
            conso=0
            s+=new_str[i]      
    if conso!=0: s+=str(conso)
    print(strr[0].upper()+s)