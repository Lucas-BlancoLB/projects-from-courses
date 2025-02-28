````python
# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Lucas"
age = 25
height = 1.84  # m
is_student = True

age = str(age)
age += '1'
print(age)


name = ''
name = bool(name)
print(name)
````

````python
# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("What's your name: ")
age = int(input("How old are you: "))

bday = age + 1

print(f"Hello {name}!")
print('HAPPY BIRTHDAY!!')
print(f"You are {bday} years old")
````