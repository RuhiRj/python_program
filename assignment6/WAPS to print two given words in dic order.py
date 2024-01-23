#Write a python script to print two given words in dictionary order
print("enter the two words")
a,b=input(),input()
print((a,b) if a>b else (b,a)) 
