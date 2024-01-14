import tkinter as tk
from tkinter import messagebox
import ast
import random
import pyperclip
# {"site":{"login": "password"}}



FONT_NAME = "Courier"
entries_list =[]
# ---------------------------- PASSWORD GENERATOR ------------------------------- #



def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for num in range(nr_letters)] + [random.choice(numbers) for num2 in
                                                                             range(nr_numbers)] \
                    + [random.choice(symbols)]

    random.shuffle(password_list)

    password = "".join(password_list)

    entries_list[2].delete(0, tk.END)
    entries_list[2].insert(tk.END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def is_ok_to_save():
    return messagebox.askokcancel(title=entries_list[0].get(), message=f"These are the details entered: \n"
                                                                        f"Login: {entries_list[1].get()}\n"
                                                                        f"Password: {entries_list[2].get()}\n"
                                                                        f"Is it okay to save?")

def saving_password():
    site, login, code = entries_list[0].get(), entries_list[1].get(), entries_list[2].get()
    if site and login and code != "":
        delete = False
        with open("passwords_saved.txt", mode="r") as file:
            rd_data = file.read()
            passwords_saved = ast.literal_eval(rd_data)

        # check if the key is in the dictionary
        if site in passwords_saved:
            #check if the value is in dictionary[KEY][key*] - key* is the key for dict in dict e.g. {KEY:{key*:value}}
            if code in passwords_saved[site][login]:
                messagebox.showinfo(title=site, message="There`s already a entry for that login and password")
                delete = False

            else:
                if is_ok_to_save():
                    passwords_saved[site][login] = code
                    wr_data = open("passwords_saved.txt", mode="w")
                    wr_data.write(str(passwords_saved))
                    wr_data.close()
                    delete = True
        # if not then add a new key with new values
        else:
            if is_ok_to_save():
                passwords_saved[site] = {login: code}
                wr_data = open("passwords_saved.txt", mode="w")
                wr_data.write(str(passwords_saved))
                wr_data.close()
                delete = True

        if delete:
            entries_list[0].delete(0, tk.END), entries_list[2].delete(0, tk.END)
    else:
        messagebox.showinfo(title="invalid input", message='Please use all fields')
# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Password Manager")
# root.geometry("240x240")
root.config( pady=20, padx=20, bg='white')

canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg='white')
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 95,image=logo,)
canvas.grid(row=0, column=0)


# In frame
frame = tk.Frame(master=root, bg='white')
frame.grid(row=1, column=0)

# texts labels in frame
lb_txt = [" Website:", '   Login:', "Password:"]
# x and y position
pos_txt = [(0, 0), (1, 0), (2, 0)]
##
# Entry strings
web_ent = ["e.g: YouTube.com", "youremail@gmail.com", ""]
# Entry positions and column span: x, y, n
pos_colspan_ent = [(0, 1, 2, 50), (1,1, 2, 50), (2,1, 1, 31)]

# Labels
for position, msg in zip(pos_txt, lb_txt):
    x,y = position
    text_label = tk.Label(master=frame , text=msg, font=(FONT_NAME, 15), bg='white')
    text_label.grid(row=x, column=y, sticky='w')

# Entries
for pos_colspan, msg in zip(pos_colspan_ent, web_ent):
    x, y , n, w = pos_colspan
    web_entry = tk.Entry(master=frame, width=w, bg='white')
    web_entry.insert(tk.END, string=msg)
    web_entry.grid(row=x, column=y, columnspan=n)
    entries_list.append(web_entry)



print(entries_list)
# Buttons
new_pass = tk.Button(master=frame, text="Generate Password", bg='white', command=generate_password)
new_pass.grid(row=2, column=2)

add_pass = tk.Button(master=frame, text="Add", width=42, bg='white', command=saving_password )
add_pass.grid(row=3, column=1, columnspan=2)
root.mainloop()