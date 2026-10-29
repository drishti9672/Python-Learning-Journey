"""take input of a number and check if its palindrome or not"""
a=int(input("enter a number:"))
# b=0
# while a>0:
#     b= b*10 + a%10 
#     a//=10
# if a==b:
#     print("the number is a palindrome")
# else:
#     print("number is not a palindrome")

#this code will always give not a palindrome 
#as during code you just cahnge the value to 
#a to zero hence first you have to make a copy
#and then compare b with it
b=0
copy=a
while a>0:
     b= b*10 + a%10 
     a//=10
if copy==b:
     print("the number is a palindrome")
else:
     print("number is not a palindrome")
