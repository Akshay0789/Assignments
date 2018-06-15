#1
a=a/(a-3)
print(a)

a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except:
    print("div by 0 error")

#2
try:
    l=[1,2,3]
    print(l[3])
except:
    print()


#3
Traceback (most recent call last):
An exception
  File "C:/Users/Akshay/PycharmProjects/ass_no-3/ass_13.py", line 22, in <module>
    raise NameError("Hi there")
NameError: Hi there

#4
-5.0
a/b result in 0




#5
import error
import ClassA
from FileA import ClassA
from FileA import *


value error
import sys
randomList = ['a',2]
for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()


#6
class error(Exception):
    """base class for other exeption"""
    pass
class ValueTooSmallError(error):
    """raised when the age is less then 18"""
    pass

age=18
while True:
    try:
        i_num = int(input("enter the age"))
        if i_num < age:
            raise ValueTooSmallError
        break
    except ValueTooSmallError :
        print("the age is less then 18,try again!")
        print()
print("congratulation,you are greater then 18")





