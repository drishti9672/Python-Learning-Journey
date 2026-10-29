import random
num= random.randint(1,10)
tries=0
while True:
    guess=int(input("enter your number:"))

    if num== guess:
        tries+=1
        print(f"you are correct you guess the number in {tries}tries")
    elif num>guess:
        tries+=1
        print("you are incorrect go a little higher")
    elif num<guess:
        tries+=1
        print("you are incorrect go a little lower")
    else:
        print("you are wrong")
