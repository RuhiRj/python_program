#Write a python script to check whether a given number is even or odd
"""n=int(input("enter the number"))
if n%2==0:
    print("no is even")
else:
    print("no is odd")"""    
print("no is even" if int(input("enter the number"))%2==0 else "no not is even") 
print("no is not even" if int(input("enter the number"))%2 else "no is even")   