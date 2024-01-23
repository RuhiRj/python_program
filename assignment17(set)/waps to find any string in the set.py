"""Write a Python script to find if “Python” is present in the set thisset = {"Java",
"Python", "Django"}"""
s={"Java","Python","Django"}
s1={e for e in s if e in "Python"}
print(s1)
