"""Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""
year=int(input("enter the year"))
if year%400!=0:
    print("non century leap year")
if year%400==0:
    print("century leap year")
if year%100!=0 and year%4!=0:
    print("non century non leap year")
if year%100==0 and year%4!=0:
    print("century non leap year")            