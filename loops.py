 # repeat a code of block for a given range

for i in range(5,11,1):
    print(i)

#for 50 to -12
for i in range(50,-13,-1):
    print(i)

#table of 8
for i in range(8,81,8):
    print(i)

#take input from user to print the table of given no by user
n=int(input("enter a number:"))
for i in range(n,(n*10)+1,n):
    print(i)

#on stringd
name="Drishti"
for i in range(0,5,1):
    print(name[i])

for i in range(len(name)):
    print(name[i])
"""also be done like this"""
for i in name:
    print(i)
