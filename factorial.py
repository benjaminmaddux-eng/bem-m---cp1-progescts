#benjamin maddux factorial calculator cumputer programing ms larose
import math
def thing():
    bean=int(input("number: "))
    if bean == 0:
        print("0=1")
        return
    ting= list(map(math.factorial, [bean])) 
    othering=ting[0]
    sting="*".join(str(b) for b in range(bean,0,-1))

    print(f"{sting}={othering}")
thing()