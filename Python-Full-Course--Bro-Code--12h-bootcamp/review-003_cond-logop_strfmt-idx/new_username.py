# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Create a new  username: ")

if len(username) > 12:
    print("Too long")
elif username.count(' '):
    print("Can't use spaces")
elif not username.isalpha():
    print("Can't use digits")
else:
    print("Valid username")