1. calculator.py
2. weight_converter.py
3. temperature_conversion.py
4. new_username.py


# CONDITIONS 
```python
#  if = Do some code only IF some condition is True
#       Else do something else

age = int(input("Enter your age: "))

if age >= 100:  # The reading order matters—don't forget that
    print("You are too old to sign up")
elif age >= 18:
    print("Here's your Credit Card")
elif age < 0:
    print("try it again, when you're alive")
else:
    print("You must be 18+ to sign up")
```
```python
response = input("Would you like food? (Y/N): ")

if response.capitalize() == 'Y':
    print('Have some food!')
else:
    print('No food for you!')
```
```python
name = input('Enter your name: ')

if name:
    print(f'Hello {name}!')
else:
    print("you did not type in your name!")
    
    
online = bool(input('Are You Online (True/False)?: '))

if online:
    print('The user is online')
else:
    print('The user is offline')
```
# Conditional Expression
```python
# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y


character = '1'  # type 'str'  letters or numbers
print("Letter" if character.isalpha() else "Number")  # x if condition else Y

num = 4  # type 'int'
print(f'{num} is Even' if num % 2 == 0 else f'{num} is Odd' )

a = 4
b = -8

max_value = a if  a > b  else b
min_value = a if  a < b else b
print(f"Greater value: {max_value}\nLess value: {min_value}")

age = 25
status = 'Adult' if age >= 18 else 'Minor'
print(status)

temperature = 20  # °C
weather = 'Hot' if temperature > 20 else 'Cold'
print(weather)

user_role = "Admin"
user_type = "Admin" if user_role == "Admin" else "Standard"
print(user_type)
```

# LOGICAL OPERATORS 
```python
# Logical Operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = Inverts the condition (not False, not True)


temp = 25  # 40  -5
is_raining = False  # True

if temp > 35 or temp < 0 or is_raining:  # If any operator is True then condition is True
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")


temp = 25  # 30,  0
is_sunny = True  # False

if temp >= 28 and is_sunny:  # if both operators are True then condition is True
    print("It is HOT outside, YIKES")
    print("And It's SUNNY")
elif temp <= 0 and is_sunny:
    print("It's COLD outside, cool")
    print("And It's SUNNY")
elif 28 > temp > 0 and is_sunny:
    print("It's WARM outside, okay..")
    print("And It's SUNNY")
elif temp >= 28 and not is_sunny:  # if both operator are True... one positive one Negative
    print("It is HOT outside, YIKES")
    print("And It's CLOUDY")
elif temp <= 0 and not is_sunny:
    print("It's COLD outside, cool")
    print("And It's CLOUDY")
elif 28 > temp > 0 and not is_sunny:
    print("It's WARM outside, okay..")
    print("And It's CLOUDY")
```
# String Methods
```python
#  String Methods

name = input("Enter your full name: ")  # 'My Name Is'
result = len(name)  # result: 10

name.find(' ')  # result: 2
name.rfind(' ')  # result: 7    r means reverse, so look for the last one

name.capitalize()  # result: My name is    Capitalize the first latter
name.upper()  # result: MY NAME IS
name.title()  # result: My Name Is
name.lower()  # result: my name is

name.isnumeric()  # result: False    If my 'str' were fully numeric it would return True
name.isalpha()  # result: False    There are spaces in 'My Name Is'
name.isspace()

name.count(' ')  # result: 2  it counted the spaces in 'My Name Is'
name.replace(__old='My Name Is', __new='My name is Lucas' )


# FOR MORE
print(help(str))
```
# Indexing
```python
# Indexing = Accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

credit_number[0]  # output: 1
credit_number[1]  # output: 2
credit_number[2]  # output: 3

credit_number[0:4]  # output: 1234
credit_number[5:9]  # output: 5678
credit_number[5:]  # output: 5678-9012-3456

credit_number[-1]  # output: 6
credit_number[-2]  # output: 5
credit_number[-4:]  # output: 3456

credit_number[::-1]  # output: 6543-2109-8765-4321
credit_number[4:-4:5]  # output: ---

```
# Format Specifiers
```python
# Format Specifiers = {:flags} format a value based oon what
#                              flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator


price1 = 3.14159
price2 = -987.65
price3 = 12.34


print(f"Price 1 is ${price1:.1f}")  # Price 1 is $3.1
print(f"Price 2 is ${price2:.2f}")  # Price 2 is $-987.65
print(f"Price 3 is ${price3:.3f}")  # Price 3 is $12.340

print(f"Price 1 is ${price1:0}")    # Price 1 is $3.14159
print(f"Price 2 is ${price2:10}")   # Price 2 is $   -987.65
print(f"Price 3 is ${price3:020}")  # Price 3 is $00000000000000012.34

print(f"Price 1 is ${price1:^015}")  # Price 1 is $00003.141590000
print(f"Price 2 is ${price2:<015}")  # Price 2 is $-987.6500000000
print(f"Price 3 is ${price3:>15}")   # Price 3 is $          12.34
print(f"Price 3 is ${price3:=15}")   # Price 3 is $          12.34

print(f"Price 1 is ${price1:+}")  # Price 1 is $+3.14159
print(f"Price 2 is ${price2:+}")  # Price 2 is $-987.65
print(f"Price 3 is ${price3:+}")  # Price 3 is $+12.34

print(f"Price 1 is ${price1: }")  # Price 1 is $ 3.14159
print(f"Price 2 is ${price2: }")  # Price 2 is $-987.65
print(f"Price 3 is ${price3: }")  # Price 3 is $ 12.34

price1__ = 3000.14159
price2__ = -9870.65
price3__ = 1200.34

print(f"Price 1 is ${price1__:,}")  # Price 1 is $3,000.14159
print(f"Price 2 is ${price2__:,}")  # Price 2 is $-9,870.65
print(f"Price 3 is ${price3__:,}")  # Price 3 is $1,200.34

print(f"Price 1 is ${price1__:^ 15,.2f}")  # Price 1 is $    3,000.14
print(f"Price 2 is ${price2__:^+15,.2f}")  # Price 2 is $   -9,870.65
print(f"Price 3 is ${price3__:^+15,.2f}")  # Price 3 is $   +1,200.34
```