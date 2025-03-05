# Weight Converter  #CONDITIONS


weight = float(input("Enter your Weight in kg: "))
unit = input("Enter used Unit (kg, lb): ").lower()
if unit == 'lb':
    weight *=  0.4536
    unit = 'Kgs'
elif unit =='kg':
    weight /= 0.4536
    unit = 'Lbs'
else:
    print(f"Bad input: unit '{unit}'")
if unit in ('Kgs', 'Lbs'):
    print(f"Your Weight is {round(weight, 2)} {unit}")
