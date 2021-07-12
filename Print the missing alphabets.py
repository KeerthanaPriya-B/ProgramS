s=input()
alpha='abcdefghijklmnopqrstuvwxyz'
missing=""
for i in alpha:
    if i not in s:
        missing+=i
print(missing)