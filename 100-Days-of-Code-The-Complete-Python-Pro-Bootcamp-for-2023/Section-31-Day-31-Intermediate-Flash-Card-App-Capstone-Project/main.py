import pandas as pd
import tkinter as tk
from random import randint
from PIL import ImageTk
BACKGROUND_COLOR = "#B1DDC6"
# -------------------------------- import data n create csv --------------------------------

def find_max_len_in_line(path):
    biggest_str = ""
    word_str = ""
    with open(path) as file:
        lines = file.read().splitlines()

        # max_len takes the biggest value (len) from the lines
        max_len = max(len(x) for x in lines)
        for i in range(1,len(lines), 2):
            if i % 2 == 0: print(True)

            line = lines[i]
            if len(line) > len(word_str):
                word_str = line
        for line in lines:

            if len(line) > len(biggest_str):
                biggest_str = line
        print(max_len, word_str ,biggest_str)

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
meaning_on_screen = True
df = pd.read_csv("5k most used.csv", index_col=0)


def random_data_row():
    num = randint(0, 4874)
    return df.iloc[num]["English"], df.iloc[num]["Meaning"]

def check_button_pressed():
    word, _ = random_data_row()
    canvas.itemconfig(backgroundImg ,image=canvas_image)
    text_label.config(text=word, font=("Ariel", 60, "bold")), front_label.config(text="ENGLISH")

def wrong_button_pressed():
    word, _ = random_data_row()
    # canvas_image1 = canvas_image()
    back_card1 = back_card()
    canvas.itemconfig(backgroundImg, image=back_card1)
    text_label.config(text=word, font=("Ariel", 60, "bold")), front_label.config(text="ENGLISH")

def view_button_pressed():
    if front_label["text"] == "ENGLISH":
        var = text_label["text"].lower()
        mask = df[df["English"] == var.lower()]
        for  row in mask.itertuples(index=False):
            word, mean = row.English, row.Meaning

        text_label.config(text=formatted_text(50, mean), font=("Arial", 20, "bold")), front_label.config(text=word)


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

    canvas.create_image((0,0), anchor=tk.NW, image=back_card())
    front_label.config(text=word)
    text_label.config(text=formatted_str, font=("Ariel", 20, "bold"))



# -------------------------------- UI interface --------------------------------
# TODO two buttons; one label; one text box
# root
root = tk.Tk()
root.title("English Flashcard")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# canvas
def back_card():
    card_back = ImageTk.PhotoImage(file="images/card_back.png")
    return card_back
def canvas_image():
    canvas_image = ImageTk.PhotoImage(file="images/card_front.png")
    return canvas_image
canvas_image = canvas_image()
print(canvas_image)
canvas = tk.Canvas(width=canvas_image.width(), height=canvas_image.height(), bg=BACKGROUND_COLOR, highlightthickness=0)
backgroundImg = canvas.create_image(0,0, anchor=tk.NW ,image=canvas_image)
canvas.grid(row=0, column=0)

front_label = tk.Label(master=canvas, text="ENGLISH", font=("Ariel", 40, "italic"), bg="white")
front_label.place(x=400, y=75, anchor=tk.CENTER)



text_label = tk.Label(master=canvas, text="Be",font=("Arial", 60, "bold") ,bg="white")
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