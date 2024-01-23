##Write a recursive python function to print first N odd natural numbers
print("enter the natural no")
n=int(input())
def oddN(n):
    if n==0:
        return 1
    oddN(n-1)
    print(2*n-1)
oddN(n)              