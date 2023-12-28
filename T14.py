import math
h=int (input("Enter the hour:"))
m=int (input("Enter the minutes:"))
s=int (input("Enter the second:"))
print(h,":",m,":",s)
a=h*3600
print("hour to seconds:",a)
b=m*60
print("minuts to seconds:",b)
time=a+b+s
print(time,"seconds")

