# fileNotFound
# with open("a_file.txt", mode="r") as file:
#     file.read()

# KeyError
# a_dictionaru = {"key": "value"}
# value = a_dictionaru["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

try:  # Something that might cause an exception
    pass
except:  # Do this if there was an exception
    pass
else:  # Do this if there were no exceptions
    pass
finally:  # Do this no matter what happens
    pass
# raise KeyError("str") give a Key_Error that will show up cuz I want so

#
##
#

# FileNotFound

try:
    file = open("a_file.txt")

except:
    file = open("a_file.txt", mode="w")
    file.write("something here")

##

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["adsdwqdqw"])  # it won't show the error
except:
    file = open("a_file.txt", mode="w")  # it writes file
    file.write("something here")

##

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["adsdwqdqw"])
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("something here")

except KeyError as key_message:  # to get what went wrong
    print(f"that key {key_message} does not exist.")

else:  # it won't work if there's an error in try:
    content = file.read()
    print(content)

##

try:
    file = open("a_file.txt")  # If there's an a_file.txt to read
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])  # KeyError fixed
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("something here")

except KeyError as key_message:  # to get what went wrong
    print(f"that key {key_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:  # If it succeeds or its failure. It will run
    file.close()
    print("File was closed.")
    # raise KeyError("This is an error that I made up")

##

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldn't be over 3 meters.")

bmi = pow(weight / height, 2)
print(bmi)

