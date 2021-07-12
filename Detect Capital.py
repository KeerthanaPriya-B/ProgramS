n=input()
if(n.isupper() or n.islower() or (n[0].isupper() and n[1:].islower())):
    print("true")
else:
    print("false")