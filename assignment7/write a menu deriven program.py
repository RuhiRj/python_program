"""Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
choice=str(input("enter the operation who user wants"))
match choice:
    case "addition":
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print("Addition=",a+b)
    case "subtraction":
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print("subtraction=",a-b)
    case "multiplication":
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print("multiplicatio=",a*b)
    case "division":
        a=int(input("enter the number"))
        b=int(input("enter the number"))
        print("division=",a/b)        
        


    



