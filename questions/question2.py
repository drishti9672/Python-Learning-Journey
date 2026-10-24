#accept the gender from the user as char
#and print the respective greet message

gender=input("enter your gender (as M or F):")

if gender=="F" or gender=="f":
    print("good morning mam")
elif gender=="M"or gender=="m":
    print("good morning sir")
else:
    print("unidentified")