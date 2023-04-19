#was to create list using createlist().count and print even odd number in the list using UDF even odd.


def evenodd(k):
    even,odd=[],[]
    count1,count2=0,0
    for i in k:
        if i%2==0:
            even.apprnd(i)
            count1+1
        else:
            odd.append(i)
            count2+=2
    print(f"The even number are  {count1} and number:")
    printlist(even)

    print(f"The odd number are {count2} and numbers:")
    printlist(odd)

def printlist(b):
        for i in b:
             print(i)


def createlist():
        a=[]
        b=int(input("How many number you wantto enetr in list:"))
        for i in range(b):
            c=int(input("Enter anumber:"))
            a.append(c)
        evenodd(a)

createlist()
