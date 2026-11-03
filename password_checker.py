#benjamin maddux computer programing ms larose
import string
lon=False
uper=False
low=False
speed=False
dig=False
strength=0
spead=["!","@","#","$","%","^","&","*"]
pas=str(input("password: "))
if len(pas) >= 8:
    lon = True
    print("long enough")
else:
    lon = False
    print("not long enough")
if any(char.islower() for char in pas):
    low=True
    print("it has lowercase")
else:
    low=False
    print("this dose not have lowercase")
if any(char.isupper() for char in pas):
    uper=True
    print("this password has uppercase")
else:
    uper=False
    print("this password doesnt have uppercase")
if pas.isdigit:
    dig=True
    print("this password has numbers")
else:
    dig=False
    print("this password dosnt have numbers")
if any(char.isdigit() for char in pas):
    speed=True
    print("this password has special characetrs")
else:
    speed=False
    print("this password dosnt have special characters")
if lon == True:
    strength += 1
if low == True:
    strength += 1
if uper == True:
    strength += 1
if dig == True:
    strength += 1
if speed == True:
    strength += 1
print(f"your password strenght: {strength}")
if strength == 0:
    print("not a good password")
if strength >= 1 and strength <= 3:
    print("this is a ok password")
if strength >= 4:
    print("realy good pasword")