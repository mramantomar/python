n= int(input("enter number to be reversed "))
rev =0
i=n
while(n>0):
     rev=(rev*10)+n%10 
     n=n//10 
print("reverse number",rev)
if(rev == i):
     print("palidrom number")
else:
    print("not a palindrome number")
