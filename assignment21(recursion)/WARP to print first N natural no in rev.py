#Write a recursive python function to print first N natural numbers in reverse order
print("enter the natural no")
n=int(input())
def revN(n):
    if n>0:
        print(n)
        revN(n-1)
revN(n)  
   