#to solve the quadratic eq
import cmath
a=1
b=5
c=6

d = (b**2)-(4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution of {0} and {1} is".format(sol1,sol2))