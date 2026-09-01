#benjamin madduxs average grade project
while True:
    try: 
        class1=float(input("grade for first period   "))
    except:
        print("not a number")
    else:
        break
while True:
    try: 
        class2=float(input("grade for second period   "))
    except:
        print("not a number")
    else:
        break
while True:
    try: 
        class3=float(input("grade for third period    "))
    except:
        print("not a number")
    else:
        break
while True:
    try: 
        class4=float(input("grade for forth period    "))
    except:
        print("not a number")
    else:
        break
while True:
    try: 
        class5=float(input("grade for fith period    "))
    except:
        print("not a number")
    else:
        break
while True:
    try: 
        class6=float(input("grade for sixth period    "))
    except:
        print("not a number")
    else:
        break
while True:
    try: 
        class7=float(input("grade for seventh period    "))
    except:
        print("not a number")
    else:
        break
addofall=class1+class2+class3+class4+class5+class6+class7
lastgpa=float(addofall/7)
roundlast=round(lastgpa,2)
print("unrounded GPA:    " ,lastgpa)
print("rounded GPA:    " ,roundlast)

