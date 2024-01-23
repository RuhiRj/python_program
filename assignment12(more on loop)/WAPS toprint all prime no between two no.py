"""Write a python script to print all Prime numbers between two given numbers (both
values inclusive)
n=int(input("enter the number"))
m=int(input("enter the number"))
count=0
for a in range(n,m):
    if a>1:
        for i in range(2,a):
           if a%i==0:
              break
        else:
           count+=1
           print("prime=",a)
           print("count=",count)"""
#Write a python script to find next prime number of a given number
n=int(input("enter the number"))
for a in range(2,n):
    if n%a==0:
        break
    print("not prime",n)
else:
  print("prime=",n)    

           