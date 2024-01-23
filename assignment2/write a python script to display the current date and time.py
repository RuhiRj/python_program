"""Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM"""
from datetime import datetime
d=datetime.today()
print(d)
dt=d.strftime("%B %d %Y")
print(dt)
dtt=d.strftime("%d/%b/%Y")
print(dtt)
r=d.strftime("%H:%M:%S")
print(r)
e=d.strftime("%I:%M:%p")
print(e)