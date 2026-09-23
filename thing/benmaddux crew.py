#benjamin maddux crew shares project
import random
while True:
    try:
        pirites=int(input("how many prirates do you have: "))
    except:
        print("not a number")
    else:
        break
units=random.randint(500,5000)
yandushare= round(units*0.13,2)
remain1=units-yandushare
petershare=round(remain1 * 0.11 ,2)
remain2= remain1 - petershare
crewshare=round(remain2/pirites, 2)
print(f"units taken: {units}")
print(f"yandu share: {yandushare}")
print(f"peters share: {petershare}")
print(f"crews share: {crewshare}")