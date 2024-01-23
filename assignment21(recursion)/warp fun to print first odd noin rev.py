#Write a recursive python function to print first N odd natural numbers in reverse order
print("enter the natural numbers")
n=int(input())
def revN(n):
    if n==0:
        return 1
    print(2*n-1)
    revN(n-1)
revN(n)    