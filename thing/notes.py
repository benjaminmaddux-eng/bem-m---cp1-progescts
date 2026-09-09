#tip calculator
'''bill=input("money here= ")
tip_tax=15/100
result=tip_tax % bill
print(result)




#var project


name=input("input name=")


print("sorry I ment  " + name)

age = 14

print("wow you are" ,age)
print("oh sorry i missed your birthday what age are you now?")
age +=1
print("ohh so your" ,age)'''

#benjamin maddux ms larsoe 
firstname=input("put in your fist name:   ")
lastname=input("put in your last name:   ")
while True:
    try:
        phonenum=int(input("phone number:   "))
    except:
        print("not a number")
    else:
        break

while True:
    try:
        gpa=float(input("grade point average:   "))
    except:
        print("not a number")
    else:
        break
phonenum3=(phonenum.split(3,6))
gparound=round(gpa,2)
firstcap=firstname.capitalize
lastcap=lastname.capitalize
print("".join([firstcap,lastcap]))
print(phonenum3)
print(gparound)