# Temperature Conversion  #CONDITIONS


temperature = float(input("Enter Your Temperature: "))
unit = input("Enter Your Unit (F, C): ").title()

if unit == 'F':
    temperature = (temperature - 32) * 5/9
    print(f"{round(temperature, 2)}°C.")
elif unit == 'C':
    temperature = (temperature *9/5) + 32
    print(f"{round(temperature, 2)}°F.")
else:
    print(F"Bad Unit typed: '{unit}'")
