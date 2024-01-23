#Write a python script to calculate sum of first N odd natural numbers
n=int(input("enter the number"))
sum=0
i=1
while i<=2*n:
    sum=sum+i
    i+=2
print(sum)          