#benjamin debug with debugger ms larose
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8) 
quantity = int(input("How many would you like? "))# this needs a int

total = price * quantity

discounted_total = total- (total * 0.10)#you jsut need to substract the total by 10%

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)# the subtraction was wrong

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name)#the variable was spelled wrong
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(round(discounted_total,2 )))#you need to print the total
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits")#there wasnt a parenthises closing it