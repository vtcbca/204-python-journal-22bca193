#write a scrpit to check if the list contain three consecutive common numbers in python using udf.


def consecutivecoomon(n):
    count=0
    b=[]
    for i in range(len(n)-2):
        if n[i]==n[i+1] and n[i+1]==n[i+1]==n[i+2]:
            b.append(n[i])
            count+=1
        if count>0:
            print(f"consecutive common number in list {n} as folow:{b}")
        else:
            print("No consecutive number in list!!")
def takeinput():
    a=[]
    b=int(input("How many number you want to enter in list:"))
    for i in range(b):
        c=int(input("Enter value:"))
        a.append(c)
    consecutivecoomon(a)

takeinput()