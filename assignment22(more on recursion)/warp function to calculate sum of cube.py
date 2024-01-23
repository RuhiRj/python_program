#Write a recursive python function to calculate sum of cubes of first N natural numbers
print("enter the number")
n=int(input())
def sumev(n):
    if n==1:
        return 1
    return (n**3)+sumev(n-1)
s=sumev(n)
print(s)