#break and continue in loops
for i in range(1,21):
    if i==5:
        break
    else:
        print(i)

for i in range(1,21):
    if i==5:
        continue
    else:
        print(i)


for i in range(1,21):
    if i ==15:
        print("else statement is executed")
        break
    else:
        print(i)
else:
    print("break statement is not executed")



for i in range(1,21):
    if i ==56:
        print("else statement is executed")
        break
    else:
        print(i)
else:
    print("break statement is not executed")