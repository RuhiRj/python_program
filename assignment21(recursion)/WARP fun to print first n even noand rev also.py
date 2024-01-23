#Write a recursive python function to print first N even natural numbers.
print("enter the number")
n=int(input())
def evenN(n):
    if n==0:
        return 1
    evenN(n-1)
    print(2*n)
evenN(n)   
#Write a recursive python function to print first N even natural numbers in reverse order.
print("enter the number")
n=int(input())
def revN(n):
    if n==0:
        return 1
    print(2*n)
    revN(n-1)
revN(n)         