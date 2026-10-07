#benjamin maddux factorial calculator cumputer programing ms larose
import math
def times(number):
    return math.factorial(number)
while True:
    try:
        num=int(input("number:"))
    except:
        print("try again")
    else:
        break
rage=range(1,num)
ranger=list(map(len, rage))
print(ranger)