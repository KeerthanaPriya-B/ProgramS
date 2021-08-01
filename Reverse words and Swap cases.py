def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    rev=sentence.split()
    strr=""
    space,string=" ",""
    for i in range(len(rev)):
        strr=space+rev[i]+strr
    new=strr.strip()
    for i in new:
        if(i.isupper()):
            string+=i.lower()
        elif(i.islower()):
            string+=i.upper()
        else:
            string+=i
    return string
    
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
