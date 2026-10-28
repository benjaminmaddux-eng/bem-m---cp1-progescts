#benjamin maddux computer programing ms larose
sepd=["!","@","#","%","^","*"]
safty_rating=0
thing=list(input("password:"))
uper = False
slower = False
if 8<=len(thing):
    safty_rating += 1
for n in thing:
    if str.isupper(n):
        uper = True
if uper == True:
    safty_rating += 1
for n in thing:
    if str.islower:
        slower=True
if slower == True:
    safty_rating += 1
for n in thing:
    if str.isdigit:
        safty_rating +=1
for n in thing:
    if n == sepd:
        safty_rating += 1
print("your safty rating: ",safty_rating)
if safty_rating <= 3:
    print("bad password")
if safty_rating > 4:
    print("good password")