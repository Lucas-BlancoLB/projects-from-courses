import math


# Circumference of a Circle

radius = float(input("Tell me the radius os a circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}")


# Area of a Circle

radius = float(input("Tell me the radius os a circle: "))

area = math.pi * radius ** 2

print(f"The area is {round(area, 2)}")


# The Hypotenuse of a Triangle

base = float(input("Tell me the Base num: "))
length = float(input("Tell me the Length: "))

calc = math.sqrt(pow(base, 2) + pow(length, 2))
print(f"The hypotenuse is {round(calc, 2):.10f}")
