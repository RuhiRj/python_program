#Write a python script to print first N odd natural numbers
for a in range(1,2*int(input("enter the number")),2):
    print(a)
#Write a python script to print squares of first N natural numbers.
for a in range(1,int(input("enter the number")),1):
    print(a*a)    
#Write a python script to print cubes of first N natural numbers.
for a in range(1,int(input("enter the number")),1):
    print(a*a*a) 
    """Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45"""
n=range(15,45)   
for a in n:
    if(n//2==0 or n//3==0):
        continue
    print(n)
