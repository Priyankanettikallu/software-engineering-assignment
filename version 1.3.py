In [1]:
from math import sqrt
In [3]:
a=0
b=2
c=1
d=(b*b)-(4*a*c)
if(a==0):
    print("divide by zero error")
else:
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
    else:
        print("roots are equal")
        x1=x2=(-b/(2*a))
        print("x1= %.2f  and x2= %.2f "%(x1,x2))
divide by zero error
->bugs are fixed..... ->divide by zero error is thrown