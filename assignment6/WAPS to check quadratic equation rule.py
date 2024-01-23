"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""
a=int(input("enter the three numbers"))
b=int(input("enter the number"))
c=int(input("enter the number"))
d=b*b-4*a*c
if(d>0):
    print("roots are real and distinct")
if(d==0):
    print("roots are real and equal")
if(d<0):
    print("roots are imaginary")
