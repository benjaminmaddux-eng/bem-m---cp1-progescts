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
phonenum3=phonenum.split(3)
phonenum6=phonenum3.split(6)
gparound=round(gpa,2)
firstcap=firstname.capitalize
lastcap=lastname.capitalize
print("".join([firstcap,lastcap]))
print(phonenum6)
print(gparound)