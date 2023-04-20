#write a script to enter any sentence and print those word which is palindrom also print total number of palindrome word.
def palincount(k):
    b=k.split(" ")
    c=0
    d=[]
    for i in b:
        if(i==i[::-1]):
            c=c+1
            d.append(i)
    if c>0:
        print(f' THE NUMBER OF PALINDROME WORD IN SENTENCE IS {c} AND PALINDROME WORDS ARE:{d}.')
    else:
        print("THERE IS NO PALINDROME WORD IN SENTENCE !!!")
k=input("ENTER A SENTENCE:")
palincount(k)
