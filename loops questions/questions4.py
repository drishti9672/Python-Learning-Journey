"""check whether a number is prime or not"""
n=int(input("enter a number"))
count=0
for i in range(1,n+1):
    if n%i==0 :
        count+=1
if count==2:
    print("it is a prime number")
else:
    print("it is not a prime number")


"""reverse a string without using inbuilt functions"""
a="Drishti"
print(a[::-1])#a method to reverse a string


#using loop
b=""
for i in range(len(a)-1,-1,-1):
    b+=a[i]
print(b)

"""check string is a palindrome or not"""
c=""
for i in range(len(a)-1,-1,-1):
    c+=a[i]
if c==a:
    print("your string is a palindrome")
else:
    print("it is not a palindrome") 



"""count all letters, digits, and special
from a given string"""

string="hbruyeuiekfn4532286#$$^%$"
dig=0
char=0
spchr=0
for i in string:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        char+=1
    else:
        spchr+=1
print(f"num of alphabets-{char}\nnum of digits-{dig}\nnum of special char-{spchr}")
