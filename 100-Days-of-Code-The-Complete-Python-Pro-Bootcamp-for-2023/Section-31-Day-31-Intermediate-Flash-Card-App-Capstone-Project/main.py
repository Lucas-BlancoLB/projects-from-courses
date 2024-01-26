import pandas as pd
import tkinter as tk
from random import randint
from PIL import ImageTk
BACKGROUND_COLOR = "#B1DDC6"

# -------------------------------- import data n create csv --------------------------------

def find_max_len_in_line(path):
    biggest_str = ""
    with open(path) as file:
        lines = file.read().splitlines()

        # max_len takes the biggest value (len) from the lines
        max_len = max(len(x) for x in lines)

        for line in lines:
            if len(line) > len(biggest_str):
                biggest_str = line
        print(max_len, biggest_str)

# find_max_len_in_line("text.txt")

def convert_to_csv():
    with open("text.txt") as file:
        data_file = file.readlines()
        # a nest-list with tuple [(English, Meaning)] indance
    data = [(data_file[i].strip(), data_file[i+1].strip()) for i in range(0, len(data_file), 2)]
    # print(data)
    df = pd.DataFrame(data=data, columns=["English", "Meaning"])

    df.to_csv("5k most used.csv")

convert_to_csv()
# -------------------------------- Data manipulation --------------------------------
df = pd.read_csv("5k most used.csv", index_col=0)

def random_data_row():
    num = randint(0, 4874)
    return df.iloc[num]["English"], df.iloc[num]["Meaning"]

def check_button_pressed():
    word, _ = random_data_row()
    canvas.itemconfig(card_back ,image=canvas_image)
    text_label.config(text=word), front_label.config(text="English")

def wrong_button_pressed():
    word, _ = random_data_row()
    canvas.itemconfig(canvas_image, image=card_back)
    text_label.config(text=word), front_label.config(text="English")

def view_button_pressed():

    var = text_label["text"].lower()
    mask = df[df["English"] == var.lower()]
    print(mask)
    # print(df["English"][mask].item())
    # mask = df.loc[df["English"] == var]
    # var1, var2 = df[mask].values()
    # print(var2)
    # print(var)
# -------------------------------- Formatting text --------------------------------
def formatted_text(max_len, text):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) <= max_len:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())
    return " \n".join(lines)

def meaning_label():
    num = 50
    word = ""
    text = "LMAOO"
    formatted_str = formatted_text(num, text)

    canvas.create_image((0,0), anchor=tk.NW, image=card_back)
    front_label.config(text=word)
    text_label.config(text=formatted_str, font=("Ariel", 20, "bold"))



# -------------------------------- UI interface --------------------------------
# TODO two buttons; one label; one text box
# root
root = tk.Tk()
root.title("English Flashcard")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# canvas
card_back = ImageTk.PhotoImage(file="images/card_back.png")
canvas_image = ImageTk.PhotoImage(file="images/card_front.png")
canvas = tk.Canvas(width=canvas_image.width(), height=canvas_image.height(), bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(0,0, anchor=tk.NW ,image=canvas_image)
canvas.grid(row=0, column=0)

front_label = tk.Label(master=canvas, text="English", font=("Ariel", 40, "italic"), bg="white")
front_label.place(x=400, y=75, anchor=tk.CENTER)



text_label = tk.Label(master=canvas, text="Be",font=("Ariel", 60, "bold") ,bg="white")
text_label.place(x=400, y=263, anchor=tk.CENTER)

# Frame for buttons
frame = tk.Frame(width=700, height=200, bg=BACKGROUND_COLOR)  #adjust it
frame.grid(row=1, column=0)


image_right = ImageTk.PhotoImage(file="images/right.png")
right_button = tk.Button(master=frame ,image=image_right,  borderwidth=0, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=check_button_pressed)
right_button.grid(row=0, column=0, padx=50 )

image_view =ImageTk.PhotoImage(file="images/view-button.png")
view_button = tk.Button(master=frame, image=image_view, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR ,activebackground=BACKGROUND_COLOR, command=view_button_pressed)
view_button.grid(row=0,column=1, padx=50)

image_wrong = ImageTk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(master=frame, image=image_wrong, borderwidth=0, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=wrong_button_pressed)
wrong_button.grid(row=0,column=2, padx=50)


# meaning_label()


root.mainloop()