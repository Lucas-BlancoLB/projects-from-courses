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




























