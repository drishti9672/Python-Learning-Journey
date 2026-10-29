
#strings takes more space because strings stores
#every character with their own unicode
"""to find unicode of any string 
u can use "ord()" """

char="A"
print(ord(char))  #tells the unicode


b="7"
print(ord(b))
char1=523
print(chr(char1)) #chr() tells us about the character odf a unicode

#string indexing 
#indexing in python starts with zero- pos indexing
#it starts with -1-neg indexing

intro="I am Drishti Sharma"

print(intro[6])

#string Slicing

print(intro[6:9])
print(intro[6:9:2])
print(intro[2:9:6])


#explicit type conversions
num1=52
num1=str(num1)
print(type(num1))

num2=85
num2=bool(num2)
print(num2)
print(type(num2)) 

"""some values are considered to be false in
 python"""
#False
#0
#0.0
#""
#{}
#[]
#()


empty=""
print(bool(empty))
print(type(empty))

#implicit type conversions 
num3=12
print(12/3) #converted to float =4.0


#formatted strings

"""used to easy our formation of strings
"""
name="Drishti"
age=19
print("my name is",name,"I am ",age,"years old")


#using formatted stringd
print (f"my name is {name} I am {age} years old")


#strings takes more space because strings stores
#every character with their own unicode
"""to find unicode of any string 
u can use "ord()" """

char="A"
print(ord(char))  #tells the unicode


b="7"
print(ord(b))
char1=523
print(chr(char1)) #chr() tells us about the character odf a unicode

#string indexing 
#indexing in python starts with zero- pos indexing
#it starts with -1-neg indexing

intro="I am Drishti Sharma"

print(intro[6])

#string Slicing

print(intro[6:9])
print(intro[6:9:2])
print(intro[2:9:6])


#explicit type conversions
num1=52
num1=str(num1)
print(type(num1))

num2=85
num2=bool(num2)
print(num2)
print(type(num2)) 

"""some values are considered to be false in
 python"""
#False
#0
#0.0
#""
#{}
#[]
#()


empty=""
print(bool(empty))
print(type(empty))

#implicit type conversions 
num3=12
print(12/3) #converted to float =4.0


#formatted strings

"""used to easy our formation of strings
"""
name="Drishti"
age=19
print("my name is",name,"I am ",age,"years old")


#using formatted stringd
print (f"my name is {name} I am {age} years old")

