#this is going to be a calculatior to find the distance from the cannonball and the cannon
print("KILL THE KING he is about 1.5 miles away and you need to hit him you make 1.5-1.6 miles of wiggle room, good luck")
print("the hevyer your cannonball is the shoter it will go an average cannon ball is around 40 punds")
while True:
    try:
        ballsize=int(input("(pounds)wheight of cannonball:   "))
    except:
        print("not a number")
    else:
        break
print("if you have your angle above 180 it will go backwords(i think)")
while True:
    try:
        angle=int(input("angle of cannon:   "))
    except:
        print("not a number")
    else:
        break
print("the longer your barrel the more presure will be made increaseing how far your cannonball gose averge is aound 75 inch")
while True:
    try:
        barrelength=int(input("(inches)lenth of cannon barrel:   "))
    except:
        print("not a number")
    else:
        break
print("gunpowder makes your cannon ball go farther average amount of oz is around 30 g")
while True:
    try:
        gunpow=int(input("(ounces) gunpowder:   "))
    except:
        print("not a number")
    else:
        break
gunpow*0.3
gpg=108*gunpow
pressure=gpg/barrelength
velo1=353.4*pressure*barrelength
velocity=velo1/ballsize
x=0,1
y=1,0
import math
tangle=45
grav=float(9.81)
import math
range1=float(velocity**2*math.sin(2*tangle))
rangefromcannon=float(range1/grav)
symplyrange=round(rangefromcannon,2)
feetaway=symplyrange/12
milesaway=feetaway/5280
print(" youre cannonball landed" ,rangefromcannon, "inches from your cannon")
print("(inches)simplyed verson:  ",symplyrange)
print("feet away",feetaway)
print("miles:   ",milesaway)
while True:
    try:
    milesaway > 1.5 or milesaway < 1.6 print("GOOD JOB YOU KILLED THE KING    ▄︻テ══━一💥")
    else:
        
if (milesaway < 1.5 or milesaway > 1.6):print(" HAHAHAHAHA YOU MISSED ")