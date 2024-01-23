#Write a recursive python function to calculate sum of first N odd natural numbers
print("enter the number")
n=int(input())
def sumod(n):
    if n==1:
        return 1
    return (2*n-1)+sumod(n-1)
s=sumod(n)
print(s)