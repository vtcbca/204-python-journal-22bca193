#create a list of 5 value with filename and extension. replace extension with".c with ".py" and print new list.
def changename(n):
    filechange=[]
    p=".c"
    for i in n:
        if p in i:
           b=i.replace(".c",".py")
           filechange.append(b)
        else:
            filechange.append(i)

    print(filechange)

filesname = ["program.c","stdio.c","a.py","math.py","hpp.py"]
changename(filesname)