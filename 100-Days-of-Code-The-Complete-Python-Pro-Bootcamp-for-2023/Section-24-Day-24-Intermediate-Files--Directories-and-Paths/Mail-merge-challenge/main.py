#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    names = names.read()
    names = names.split("\n")

for i in names:
    with open("./Input/Letters/starting_letter.txt") as letter:
        letter_modded = letter.read()
        letter_modded = letter_modded[:5] + i + letter_modded[11:]
    with open("./Output/ReadyToSend/ready_to_send.txt", mode="a") as fd_letters:
        fd_letters.write(letter_modded + "\n\n\n")