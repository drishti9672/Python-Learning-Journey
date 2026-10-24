#accept a year and check if elif leap yearor not (google to find out what is a leap year)


year = int(input("tell your year:"))
if year%100==0 and year%400==0:
    print("it is a leap year")
elif year%100!=0 and year%4==0:
    print("it is a leap year")
else:
    print("it is not a leap year")