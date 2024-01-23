"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
age=int(input("enter the persion age"))
if age<=10 and age>=20:
   print("kid age")   
if age<=40:
   print("young age")
if age<=60:
   print("Experience persion")
if age>=60:
   print("senior citizen")         
