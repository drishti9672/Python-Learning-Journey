#while loops questions
"""sepearte eeach digit of number and print it on
the new line """
a=int(input("enetr a number:"))
while a>0:
    print(a%10)
    a//=10


"""accept a number and print it reverse"""
b=int(input("enter another number"))
rev=0
while b>0:
    rev = rev*10 +( b%10)
    b//=10
print(rev)
