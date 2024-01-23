"""Write a python script to reverse a number.
n=int(input("enter the number"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("reverse no=",rev)""" 
n=int(input("enter the number"))
m=int(input("enter the number"))
count=0
for a in range(n,m):
    prime=True
    for i in range(2,a):
        if(a%i==0):
            prime=False
    if prime==True:
                count+=1
                print(a)
print("count=",count)                
