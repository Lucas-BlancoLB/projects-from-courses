# Exercise 1 Rectangle Area Calc

# length = float(input('Tell me the length of your rectangle: '))
# width = float(input("Tell me it's width: "))
#
# A = width * length
#
# print(f"The Area of The Rectangle is: {A}cm²")

# Exercise 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What's the price?: "))
quantity = int(input("How many would you like to buy?: "))

calc = price * quantity

print(f"Your total is: ${calc:.2f} of {item}.")