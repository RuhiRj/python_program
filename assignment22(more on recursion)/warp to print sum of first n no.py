#Write a recursive python function to calculate sum of first N natural numbers
i=1
sum=0
print("enter 5 numbers")
while i<=5:
    n= int(input())
    if n%2:
        sum=sum+n
    i+=1
print(sum)
