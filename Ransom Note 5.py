ransomnote=sorted(input())
magazine=sorted(input())
flag=0
if(len(ransomnote)>len(magazine)):
    print("false")
else:
    for i in range(len(ransomnote)):
        if(ransomnote[i]!=magazine[i]):
            flag=1
            break
    if(flag==0):
        print("true")
    else: print("false")