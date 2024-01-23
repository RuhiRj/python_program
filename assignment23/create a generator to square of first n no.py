#4. Create a generator to produce squares of first N natural numbers
def squa(n):
    a=1
    while n:
        yield a
        b=a**a
        a+=1
        n-=1
#it=squa(5)        
#print(next(it)) 
#print(next(it))       
for e in squa(int(input("enter the number"))):
   print(e)        
