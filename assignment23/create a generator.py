#2. Create a generator to produce first n odd natural numbers
def oddnat(n):
    a=1
    while n:
        yield a
        a+=2
        n-=1
for e in oddnat(int(input("enter the number"))):
    print(e)    