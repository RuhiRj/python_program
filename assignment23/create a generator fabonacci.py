"""5.Create a generator to produce first n terms of Fibonacci series
def fibo(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for e in fibo(int(input("enter the number"))):
    print(e)"""
#6. Create a generator to produce first n prime numbers
def pri(n):
    a=2
    while n:
        yield a
        if a%n==0:
            n-=1
            return True
        else:
            return False
for e in pri(int(input("enter the number"))):
    print(e)        
                 
#8. Create an endless iterator using generator method to produce Prime numbers

            
    
