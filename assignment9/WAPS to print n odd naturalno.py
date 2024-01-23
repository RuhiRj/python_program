#Write a python script to print first N odd natural numbers
n=int(input("enter the number"))
m=1
while 2*n>=m:
    print(m)
    m+=2
#Write a python script to print first N odd natural numbers in reverse order
n=int(input("enter the number"))
while 2*n>=1:
    print(2*n-1)
    n-=1    