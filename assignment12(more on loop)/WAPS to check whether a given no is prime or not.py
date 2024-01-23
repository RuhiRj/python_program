"""Write a python script to check whether a given number is Prime or not
n=int(input("enter the number"))
if n%2==0 and n%3==0 and n%5==0:
    print("not a prime no")
else:
    print("prime")"""
#Write a python script to print all Prime numbers under 100
n=1
while 1>=n<=100:

    if n%2!=0 and n%3!=0 and n%5!=0:
            print(n)
            n+=1 
    else:
       print(n)        
        