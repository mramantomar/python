n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
if(n1>n2 and n1>n3):
    print("largest number : ",n1)
elif(n2>n1 and n2>n3):
    print("largest number : ",n2)
else:
    print("largest number :",n3)
