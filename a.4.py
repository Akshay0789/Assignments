#check weather the year is leap year or not
year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")




#square or ractangle
tgons=[[1,2,1,2],[1,1,1,1]]
squares=0
rects = 0
neithers = 0
for gon in tgons:
    if any(n <= 0 for n in gon):
        neithers+=1
        print("error!")
    elif len(set(gon)) == 1:
        squares+=1
        print("square")
    elif gon[0] == gon[2] and gon[1] == gon[3]:
        rects+=1
        print("ractangle")
    else:
        neithers+=1

#a shop will give discount............
print("enter quantity")
quantity = input()
    if quantity*100 > 1000 :
        print("cost is",((quantity*100)-(.1*quantity*100)))
    else :
        print("cost is",quantity*100)


# youngest & eldest
a = int(input("enter_age1 :"))
b = int(input("enter_age2 :"))
c= int(input("enter_age3 :"))
    if (a>b and a>c and b>c):
        print("a is eldest and c is youngest")
    elif (b>a and b>c and c>a):
        print("b is eldest and a is youngest")
    else:
        print("c is eldest and b is youngest")


#place of service
print("enter age")
age = input()
print("sex :(M or F)")
sex = input()
print("married : (Y or N)")
marry = input()
    if sex =="F" and age >= 20 and age <= 60 :
        print("urban areas only")
    elif sex == "M" and age >= 20 and age <= 40 :
        print("you can work anywhere")
    elif sex == "M" and age > 40 and age <= 60 :
        print("urban areas only")
    else:
        print(error)
