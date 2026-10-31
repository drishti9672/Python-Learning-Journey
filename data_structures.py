"""lists"""
a=[12,13,2.3,21/6,"drishti",True]
print(a[5])

##to print index values of string using loops
for i in range(len(a)):
    print(a[i])


#to know about all list methods and functons

print(dir(a))
# help(list)  #gives idea of what  function and method do


a.append("kriti")
a.insert(1,36)
print(a)

a.remove(12)#remove first occurence of element you wrote

"""tuples"""

b=("drishti",12,3.2,True,3,3)

print(b.index(12))
print(b.count(3))

c,d,e,f = (1,2,3,4)
print(c)
print(d)
print(e)
print(f)
#for making single element tuple
tuple=(3,)
print(type(tuple))
