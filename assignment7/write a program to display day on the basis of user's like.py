"""Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""
colour_name=str(input("user's favorite colour:-"))
match colour_name:
    case "I like yellow colour":
        print("monday")
    case "I like blue colour":
        print("tuesday")
    case "I like orange colour":
        print("wednesday")
    case "I like white colour":
        print("thursday")
    case "I like black colour":
        print("friday")
    case " I like red colour":
        print("saturday")
    case "_":
        print("sunday")
