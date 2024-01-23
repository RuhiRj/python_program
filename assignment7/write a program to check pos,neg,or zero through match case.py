"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""
n=int(input("enter the number"))
match n:
    case n if n>0:
         print("positive number")
    case n if n<0:
         print("negative number")
    case n if n==0:
         print("number is zero")          