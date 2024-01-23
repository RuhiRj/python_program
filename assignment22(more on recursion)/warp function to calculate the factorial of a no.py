#Write a recursive python function to calculate the factorial of a number.
print("enter the number")
n=int(input())
def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
print(fac(n))