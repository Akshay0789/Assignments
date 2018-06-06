#area of a sphare

import math
radius = input("Enter Radius: ")
print("Radius: " + str(radius))
r = float(radius)
surface = 4.0 * math.pi * (r*r)
print(" Area: " + str(round(surface,2)))

#multiplication table of 12

num = 12
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)

#power

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))


#factorial

n = 25
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print("The factorial of 23 is : ", end="")
print(fact)

#perfect number
def perfect(p):
    x=1
    s=0
    while x<p:
        if(p%x==0):
            s+=x
        x+=1
    if s==p:
        print(p,"is a perfect number")
for x in range (1,1000):
    perfect(x)