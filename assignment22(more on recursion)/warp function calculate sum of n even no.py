#Write a recursive python function to calculate sum of first N even natural numbers
print("enter the number")
n=int(input())
def sumev(n):
    if n==1:
        return 1
    return (2*n)+sumev(n-1)
s=sumev(n)
print(s)