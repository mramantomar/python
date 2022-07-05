a=[]
size=int(input("enter size of list :"))
for i in range(size):
    val =input("enter word : ")
    a.append(val)
print(a)
key=input("enter word to find frequency : ")
count=0
for i in range(size):
    if(a[i]==key):
        count=count+1

print("frequency is ",count)
