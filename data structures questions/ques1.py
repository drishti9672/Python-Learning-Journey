"""prints positive and negative elements of a list"""
l=[15,-9,52,-89,-9.3]
pos=[]
neg=[]
for i in range(len(l)):
    if l[i]>=0:
       pos.append(l[i])
        
    else:
        neg.append(l[i])
print(f"positive numbers are {pos}")
print(f"negative numbers are{neg}")



"""mean of list elements"""
sum=0

for i in l:
    sum+=i
print(sum/len(l))

"""find the greatest element and print its index too"""
great=l[0]
index=0
for i in range(len(l)):
    if l[i]>great:
        great = l[i]
        index=i
print(f"your greatest number is {great} having index{index}")


"""find the second graetest element """
great=l[0]
second_great=l[0]
for i in range(len(l)):
    if l[i]>great:
        second_great= great
        great=l[i]
print(f"the second greatest number is {second_great}")


"""check if list is sorted or not"""
list=[1,2,3,5,9,78]
for i in range(len(list)-1):
    if list[i]>list[i+1]:
        continue
    elif list[i]<list[i+1]:
        continue
    else:
        print("list is not sorted")
else:
    print("list is sorted")