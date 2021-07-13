import textwrap

def wrap(string, max_width):
    j,k,ss,find_len=0,max_width-1,"",""
    for i in range(len(string)//max_width):
        s=string[j:k+1]
        j=k+1
        k=k+max_width
        ss+=s+'\n'
        find_len+=s
    return ss+string[len(find_len):]
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)