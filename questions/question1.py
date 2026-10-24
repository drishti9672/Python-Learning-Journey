#accept two numbers and print the
#  greatest between them

num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))

if num1>num2:
    print(num1, "is greater")
elif num2>num1:
    print(num2,"is greater")
else:
    print("both are same")