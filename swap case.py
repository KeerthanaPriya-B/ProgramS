def swap_case(s):
    strr=""
    for i in s:
        if(i.isupper()):
            strr+=i.lower()
        elif(i.islower()):
            strr+=i.upper()
        else:
            strr+=i
    return strr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)