def minion_game(string):
    # your code goes here
    length=len(string)
    vowels,conso=0,0
    for i in string:
        if(i in 'AEIOU'):
            vowels+=length
        else:
            conso+=length
        length-=1
    if(vowels>conso): print("Kevin",vowels)
    elif(vowels<conso): print("Stuart",conso)
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)