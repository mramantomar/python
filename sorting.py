n=int(input("enter no of items"))
a=[]
for i in range(n):
    x= int(input("enter items in list"))
    a.append(x)
print("original array",a )
a.sort()
print("sorted array",a)
    
