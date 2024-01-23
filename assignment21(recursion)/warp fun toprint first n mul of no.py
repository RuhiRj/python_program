#Write a recursive python function to print first N multiples of a given number
print("enter the number")
n=int(input())
m=int(input())
def mul(n):
    if n==0:
        return 1
    mul(n-1)
    print(n*m)
mul(n)      