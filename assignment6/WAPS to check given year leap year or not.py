#Write a python script to check whether a given year is a leap year or not
year=int(input("enter the year"))
if year%4==0 and year%400:
    print("leap year")
else:
    print("non leap year")    