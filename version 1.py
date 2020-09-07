In [1]:
from math import sqrt
In [2]:
a=1
b=4
c=5
d=(b*b)-(4*a*c)
if(d>0):
    print("roots are real")
    x1=(((-b)+sqrt(d))/(2*a))
    x2=(((-b)-sqrt(d))/(2*a))
    print("the roots are: %f and %f" %(x1,x2))
elif(d<0):
    print("roots are imaginary")
    x1=x2=(-b/(2*a))
    j=(sqrt(-d))/(2*a)
    print("x1= %.2f + %.2f i and x2= %.2f - %.2f i"%(x1,j,x2,j))
roots are imaginary
x1= -2.00 + 1.00 i and x2= -2.00 - 1.00 i
->bugs fixed.... ->could not get complex values before