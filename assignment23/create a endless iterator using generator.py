"""7. Create an endless iterator using generator method to produce terms of Fibonacci
series"""
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
it=fib()
while True:
    ans=input("do you want to generate another element[y/n] ")
    if ans=='y':
        print(next(it))
    else:
        break 
#8. Create an endless iterator using generator method to produce Prime numbers               
