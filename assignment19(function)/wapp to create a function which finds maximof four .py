#Write a python program to create a function that finds a maximum of four numbers.
def max(a,b,c,d):
    if a>=b and a>=c and a>=d:
        print(a)
    elif b>=c and b>=d:
        print(b)
    elif c>=d:
        print(c)
    else:
        print(d)
max(7,4,5,0)
def max():
    print("enter the foure numbers")
    a=int(input()) 
    b=int(input())
    c=int(input())
    d=int(input())
    if a>=b and a>=c and a>=d:
        print(a)
    elif b>=c and b>=d:
        print(b)
    elif c>=d:
        print(c)
    else:
        print(d)
max()
                                       