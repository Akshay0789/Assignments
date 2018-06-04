#tuples

fruits = ('apple','grapes','banana','orrange',1,2,3)
print(fruits)

#1.lenght
print(len(fruits))

#2.max/min

print(max(25,45,54,365,56,32,4))
print(min(23,34,5,42,3,5465,3,4,-2,-5))

#product

product = 1
list = [1, 2, 3]
for x in list:
    product *= x




#sets

#set diffrence

setx = set(["red","green","yellow"])
sety = set(["blue","green","white"])
setz = setx & sety
print(setz)
setx = setx - setz
print(setz)

#compare
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
same_value = set(a) & set(b)
print(same_value)

#insertion of two sets

setx = set(["apple","banana"])
sety = set(["banana","orange"])
setz = setx & sety
print(setz)

#dictionaries

student={
    'marks': 100,
    'joe' : 77,
    'mia' : 45,
    'devid' : 98,
    'olivia' : 48
}
print("the marks dictionary is",student)

#sort
for key in sorted(student):
    print("%s:%s"%(key,student[key]))

#mississippi
s='MISSISSIPPI'
l=list(s)
m_count=l.count('M')
i_count=l.count('I')
s_count=l.count('S')
p_count=l.count('P')
dict={
    'M':m_count,'l':i_count,'S':s_count,'P':p_count
}
print("the created dictionary is",dict)