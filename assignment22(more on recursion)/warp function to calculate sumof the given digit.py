"""#Write a recursive python function to calculate sum of the digits of a given number
print("enter the value")
p=eval(input())
p=2500
t=2
r=3
si=p*r*t/100
print(si) 
#wapp to take student information fro the user and print it
print("enter the name ,inrollmentno,section,pecentage,roll no")
name=(input("enter the name"))
rollno=(input("enter the rollno"))
section=(input("enter the secrion"))
percentage=(input("enter the percentage"))
print(name,rollno,section,percentage)
#wapp to convert given amount into smallest possible input
print("enter the amount")
amount=int(input())
hun=amount//100
rem=amount-hun*100
fif=rem//50
rem=rem-fif*50
twin=rem//20
rem=rem-twin*20
ten=rem//10
print("hun=",hun)
print("fif=",fif)
print("twin=",twin)
print("ten=",ten)
n=1388
h=n//100
n=n%100
f=n//50
n=n%50
print(h,n,f)
#wapp to swap two number using third variable
print("enter the number")
a=int(input())
b=int(input())
c=a
a=b
b=c
print(a,b)
a,b=b,a
print(a,b)
#WAP program to convert a given integer(in seconds) to hours,minutes ,and seconds
print("enter the integer(in secounds)")
n=int(input())
m=n//60
h=m//60
m=m%60
se=n%60
print("hours=",h)
print("minutes=",m)
print("seconds=",se)
print("H:M:S-",h,m,se)
print("enter the five numbers")
a=int(input("enter the first number"))
if a%2!=0:
      print(a+a)      """
a,b,c,d,e=int(input("entre the five numbers")).split(" , ")
print(a%2==0 +b%2==0+ c%2==0+ d%2==0 +e%2==0)
     

































