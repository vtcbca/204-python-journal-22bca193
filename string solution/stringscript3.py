#write a script to create a list with 5 string and count total number of length with string using UDF
def evenstri(a):
    k=[]
    count=0
    for i in a:
         if(len(i)%2==0):
             k.append(i)
             count=count+1
     if(count>0):
            print(f'THE NUMBER OF EVEN STRING IS {count} AND STRING :{k}')
        else:
            print("NO EVEN STRING AVAILABLE!")
a=[]
for i in range(5):
    f=input(f"ENTER STRING:{i+1}:")
    k.append(f)
evenstri(a)
