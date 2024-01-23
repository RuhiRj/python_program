#Write a python script to print first M multiples of N.
n=int(input("enter the number"))
for a in range(int(input("enter the number"))):
    print(n*(a+1))
#Write a python script to print the first 10 multiples of N in reverse order.
n=int(input("enter the number"))
m=10
for a in (n*(a+1),range(m),-1):
    print(n*(a+1))

