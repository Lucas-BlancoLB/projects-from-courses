


# U can create a new file using the method open
# when  mode="w" (write) is set
# with open("create_new_text.txt", mode="w") as file:
#     file.write("Hello world\nClassic")


# Better way, u don't have to remember to close the file
# with open("C:/Users/Lucas/Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)


# # a mode append into the file
# with open("my_file.txt", mode="a") as file:
#     content = file.write("\nEl classic")
#     print(content)


###
# if u open is a good practice to close, cuz it may slow down ur pc
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()