#print integers on screen
numbers=[]
for i in range (10):
    x=int(input("enter no. \n"))
    numbers.insert(i,x)
    i+=1
print("numbers are :",numbers)


#infinite loop
l = [1]
for x in l:
   l.append(x + 1)
     print(x)


#square of the elements
s=[]
a=[1,2,3,4,5,6]
s=[]
for i in a:
  s.append(i ** 2)
print (s)

#int,float,char
myList = [ 4,'a', 'b', 'c', 1, 'd', 3,4.5,6.]
myIntList = [x for x in myList if isinstance(x, int)]
print(myIntList)
myStrList = [x for x in myList if isinstance(x, str)]
print(myStrList)
myFloatList = [x for x in myList if isinstance(x, float)]
print(myFloatList)

#prime number
i=2
for i in range(1,101) :
    while(i<100):
        j=2
        while(j<=(i/j)):
            if not (i%j):break
            j=j+1
        if(j>i/j) : print(i, "is a prime number")
        i=i+1
    print("done")

#pattern
for n in range(0,4):
    n +=1
    print ("*" *(0+n))



#create a user defined dict....
dict={}
for i in range(1,6):
    name = input("student name")
    dict.update({i:name})
    print("required dictionary")
    print (dict)



#deletion of element
a1=[]
for i in range(0,5):
    x= input("enter elements to the list :")
    a1.append(x)
s=input("enter element to be deleted")
for i in a1:
    if i==s:
        a1.remove(i)
        print("element found and removed")
        break
    else:
        print("element not found:")
