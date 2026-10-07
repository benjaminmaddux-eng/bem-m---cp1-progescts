#benjamin maddux factorial calculator cumputer programing ms larose
while True:
    try:
        num=int(input("number:"))
    except:
        print("try again")
    else:
        break
import math
answer=math.factorial(num)
print(f"this is the factorial of the number you put in: {answer}")