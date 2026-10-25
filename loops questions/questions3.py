"""print the sum of all even and odd numbers in a range seperately"""
even_sum=0
odd_sum=0
for i in range(1,10):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print(f"the sum of even numbers in range-{even_sum}")
print(f"the sum of odd numbers in range-{odd_sum}")


"""print all facttors of a number"""
n=int(input("enter a number:"))

for i in range(1,n+1):
    if n%i==0:
        print(i)

"""accept a number and check if it is a perfect num or not"""
#a num is said to be perfect num if the sum of its 
# factors is equal to the number itself
num=int(input("tell a number:"))
sum=0
for i in range(1,num+1):
    if n%i==0 :
        sum+=i
if sum==num:
    print("the number is a perfect number")
else:
    print("given number is not perfect")


