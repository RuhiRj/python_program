#Write a recursive python function to print first N natural numbers.
print("enter the natural no")
n=int(input())
def printN(n):
    if n>0:
        printN(n-1)
        print(n) 
printN(n)