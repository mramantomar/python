n=int(input("enter a number :"))
i=n
count=0
while(i>0):   #checks no of digits in a number
    i=i//10
    count=count+1
i=n
sum=0
while(i>0): 
    digit=i%10
    x=1
    product=1
    while(x<=count):  #calucalting power of each digits
        product=product*digit
        x=x+1
    sum=sum+product
    i=i//10
if(sum==n):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
