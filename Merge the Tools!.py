from collections import OrderedDict
def merge_the_tools(string, k):
    
    n,step,list=0,k,[]
    for i in range(len(string)//k):
        sub=string[n:k]
        print(''.join(OrderedDict.fromkeys(sub)))
        n=k
        k=k+step                
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)