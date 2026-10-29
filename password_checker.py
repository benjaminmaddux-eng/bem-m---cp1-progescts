#benjamin maddux computer programing ms larose
lon=False
uper=False
low=False

pas=input("password: ")
if len(pas) >= 8:
    lon=True
    print("long enough")
else:
    lon = False
    print("not long enough")
if pas.islower:
    low=True
    print("it has lowercase")
else:
    low=False
    print("this dose not have lowercase")
if pas.isupper:
    uper=True
    print("this password has uppercase")
else:
    uper=False
    print("this password doesnt have uppercase")
if pas.isdigit:
    dig=True
    print("this password has numbers")
else:
    uper=False
    print("")