# benjamin maddux what my grade 
while True:
    try:
        gradeuser=float(input("number grade (0-4.0):"))
    except:
        print("not a number")
    else:
        break
if gradeuser == 0:
    print("thats not good you have a F")
elif gradeuser >= 1.0 and gradeuser < 1.7:
    print("you have a D you should get help")
elif gradeuser >= 1.7 and gradeuser < 2.3:
    print("you have around a c grade, good job")
elif gradeuser >= 2.3 and gradeuser < 3.3:
    print("you have a B you are doing good at school and trying your hardest")
elif gradeuser >= 3.3 and gradeuser < 3.7:
    print("you have a A grade you are very smart and i respect that")
if gradeuser == 4.0:
    print("you have a A+ [nerd]")