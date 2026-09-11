#benjamin maddux la rose 1st period
print("dice roller")
sides=int(input("What size dice would you like to roll? (D4, D6, D8, D10, D12, D20):  "))
import random
roll=random.randint(1,sides)
print(f"this is what you rolled: {roll}")