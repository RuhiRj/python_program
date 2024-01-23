"""Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}"""
s1={"Java","Python","SQL"}
s2={"C","Cpp","NoSQL"}
s2.add("Java")
s2.add("Python")
print(s2)
print(s1)
s=set()
s.add("Python")
print(s)
print(type(s))