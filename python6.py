#To calculate the area of triangle
a = int(input("Enter the first number :"))
b = int(input("Enter the second  number :"))
c = int(input("Enter the third number :"))

s = (a+b+c)/2

Area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of triangle is",Area)