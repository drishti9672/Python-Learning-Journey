#functions can be iinbuilt or defined
#function is a block of reuseable code that we create
#nd it will run only when we call it

def hello():
    print("this is a hello function")

hello()


def sum(a,b):
    print(F"the sum of numbers is {a+b}")

sum(52,63)

#arguments are values which we pass to the parameters
"""arguments are of three types"""
#1=positional -(above one is example of positional arguments)
#2-key word arguments
#3-default arguments

def introduction(name,age):
    print(f"your name is {name} and age is{age}")

introduction("drishti",19)

def intro(name,age=19):
    print(f"your name is {name} and age is {age}")


intro("drishti")
intro("drishti",21)


#use functn to check a word is palindrome or not

def palindrome(str):
    rev=""

    for i in range(len(str)-1,-1,-1):
        rev+=str[i]
    if str==rev:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not a palindrome")

palindrome("naman")
palindrome("japan")

#return
def hello():
    return"hello how are you"

print(hello())

