#write a menudriven list which perfrom following operation
#1.create list of string till user choice.
#2.print string with even character in length.
#3.replace odd character of string with index no.
#4.enter start and end value and extract character from the list of string.



a=[]
q="y"
while q=="y" or q=="Y":
    print("\n1.ADD ITEAMS IN LIST .\n2.PRINT STRING WITH EVEN CHARACTER IN LENGTH.\n3.REPLACE ODD CHARACTER OF STRING WITH INDEX NO.\n4.ENTER START AND END VALUE AND EXTRAXT FROM THE STRING\n")
    c=int(input("ENTER YOUR CHOICE!!"))

    if c==1:
       a1="y"
       while a1=="y" or a1=="Y":
             i=input("ENTER A STRING YOU WANT TO ENTER:")
             a.append(i)
             a1=input("DO YOU ADD MORE STRING PRESS(y/Y)")

  elif c==2:
      b=[]
      count=0
      for i in a:
          if(len(i)%2==0);
             b.append(i)
             count+=1
     if count>0:
         print(f"STRING WITH EVEN CHARACTER IS{b}")
     else:
         print("STRING HAD NO EVEN CHARACTER IN IT.....")
 elif c==3:
      p=[]
      for i in a:
          o=[]
          for enu,j in enumerate(a):
              if enu%2==0:
                  o.append(j)
        p.append(o)
    for i in p:
        print(i)



elif c==4:
    s=int(input("ENTER START INDEX:"))
    e=int(input("ENTER END INDEX:"))
    res=" ".join([sub for sub in a])[s:e]
    print(f"YOUR STRING IS{res}")


else:
    print("ENTER A VAILD CHOICE!")

q=input("DO YOU WANT TO CONITINUE:(y/Y):")
