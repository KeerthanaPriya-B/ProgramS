n=int(input())
for i in range(n):
    n1=input().split()
    binary=bin(int(n1[0])).lstrip('0b')
    diff=16-len(binary)
    
    if(diff):
        for j in range(diff):
            binary='0'+binary
            
    if(n1[2]=='L'):
        split=binary[:int(n1[1])]
        balance=binary[int(n1[1]):]
        print(int(balance+split,2))
        
    elif(n1[2]=='R'):
        split=binary[(16-int(n1[1])):]
        balance=binary[:16-int(n1[1])]
        print(int(split+balance,2))