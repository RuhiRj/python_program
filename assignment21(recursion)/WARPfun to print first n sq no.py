#Write a recursive python function to print squares of first N natural numbers
print("enter the number")
n=int(input())
def sq(n):
    if n==0:
        return 1
    sq(n-1)
    print(n*n)
sq(n)   
#Write a recursive python function to print cubes of first N natural numbers
print("enter the number")
n=int(input())
def sq(n):
    if n==0:
        return 1
    sq(n-1)
    print(n**3)
sq(n)  

    