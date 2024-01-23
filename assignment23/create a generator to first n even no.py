#3. Create a generator to produce first n even natural numbers
def evenn(n):
    a=2
    while n:
     yield a
     a+=2
     n-=1
for e in evenn(int(input("enter the number"))):
    print(e)
