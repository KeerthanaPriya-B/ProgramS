from datetime import datetime
main=input()
date=datetime.strptime(main,"%H:%M:%S")
n=int(input())
li=[]
for i in range(n):
    new=input()
    new_date=datetime.strptime(new,"%H:%M:%S")
    strr=str(date-new_date).split(':')
    if(int(strr[0])>=1):
        if(int(strr[0])==1): 
            print(strr[0].lstrip('0')+' hour ago')
        else: 
            print(strr[0].lstrip('0')+' hours ago')
    elif(int(strr[1])>=1):
        if(int(strr[1])==1):
            print(strr[1].lstrip('0')+' minute ago')
        else: 
            print(strr[1].lstrip('0')+' minutes ago')
    elif(int(strr[2])>=1):
        if(int(strr[2])==1):
            print(strr[2].lstrip('0')+' second ago')
        else: 
            print(strr[2].lstrip('0')+' seconds ago')
    else: print('now')
            