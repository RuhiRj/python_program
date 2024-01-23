"""Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]"""
s={"Python","Django","JavaScript"}
#s.add(["Java","C"])list adding is not possible in set but update is possible for adding elements
s.update(["Java","C"])
print(s)
