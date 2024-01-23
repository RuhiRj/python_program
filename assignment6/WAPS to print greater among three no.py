"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
if a>b and a>=c:
    print(a)
if b>=c:
    print(b)
else:
    print(c)