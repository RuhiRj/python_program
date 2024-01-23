#Write a python script to calculate factorial of a given number
n=int(input("enter the number"))
fac=1
while n>=1:
    fac=fac*n
    n-=1
print(fac)    
