"""reverse for loop print n to 1"""
n=int(input("enter a number"))
for i in range(n,0,-1):
    print(i)


"""take a num as input and print its table"""

num=int(input("enter a num:"))

for i in range(num,(num*10)+1,n):
    print(i)

#if i want to write table like we really write

for i in range(1,11):  
    print(f"{n}*{i}={n*i}")


"""sum upto n terms"""

num1=int(input("enter a number:"))
sum=0
for i in range(1,num1+1):
    sum+=i
print(f"your sum is {sum}")


"""factorial of a number
"""
factorial=1
for i in range(1,num1+1):
    factorial *= i
print(f"the factorial of givrn number is{factorial}")
