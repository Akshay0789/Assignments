#import error
#import ClassA
#from FileA import ClassA
#from FileA import *



#value error
#import sys
#randomList = ['a',2]
#for entry in randomList:
 #   try:
  #      print("The entry is", entry)
   #     r = 1/int(entry)
    #    break
    #except:
     #   print("Oops!",sys.exc_info()[0],"occured.")
      #  print("Next entry.")
       # print()
#
#Traceback (most recent call last):
#An exception
 # File "C:/Users/Akshay/PycharmProjects/ass_no-3/ass_13.py", line 22, in <module>
  #  raise NameError("Hi there")
#NameError: Hi there

#
#-5.0
#a/b result in 0

a=3
if a<4:
    a=a/(a-3)
    print(a)
