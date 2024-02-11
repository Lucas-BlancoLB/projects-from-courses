import pandas as pd
import tkinter as tk
from random import randint
from PIL import ImageTk, Image


BACKGROUND_COLOR = "#B1DDC6"


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


class EnFlashCard:
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("English Flashcard")
        self.root.geometry('900x725')
        self.root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

        self.front_card = ImageTk.PhotoImage(Image.open("images/card_front.png"))
        self.back_card = ImageTk.PhotoImage(Image.open("images/card_back.png"))
        self.wrong_image = ImageTk.PhotoImage(file="images/wrong.png")
        self.right_image = ImageTk.PhotoImage(file="images/right.png")
        self.view_image = ImageTk.PhotoImage(file="images/view-button.png")
        self.canvas = None
        self.canvas_image = None
        self.title_txt = None
        self.text_txt = None
        self.to_learn_on = None
        self.load_data()
        self.db = self.load_data()
        self.to_learn_db = pd.read_csv("words_to_learn.csv", index_col=0)
        print(type(self.to_learn_db))
        self.create_ui()
    def load_data(self):
        try:
            to_learn_db = pd.read_csv("words_to_learn.csv", index_col=0)
            if not to_learn_db.empty:
                self.to_learn_on = True
                return to_learn_db
            else:
                self.to_learn_on = False
                original_df = pd.read_csv("5k most used.csv", index_col=0)
                return original_df.copy()
        except FileNotFoundError:
            df = pd.DataFrame(columns=["English", "Meaning"])
            df.to_csv("words_to_learn.csv")


    def create_ui(self):
        # User interface | widgets
        self.create_canvas()
        frame = tk.Frame( bg=BACKGROUND_COLOR)  # adjust it
        frame.grid(row=1)
        self.create_buttons(frame)
    def create_canvas(self):
        # Create a canvas for the UI
        title, _ = self.random_data_row()

        self.canvas = tk.Canvas(width=self.front_card.width(), height=self.front_card.height(), bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas_image = self.canvas.create_image(0,0, anchor=tk.NW, image=self.front_card)
        self.title_txt = self.canvas.create_text((400, 75), text="ENGLISH", anchor=tk.CENTER, font=("Ariel", 40, "italic"))
        self.text_txt = self.canvas.create_text((400, 263), text=formatted_text(21, title), anchor=tk.CENTER, font=("Arial", 60, "bold"))
        self.canvas.grid()

    def create_buttons(self, frame):
        # Create buttons for the UI
        wrong_bt = tk.Button(master=frame, image=self.wrong_image, borderwidth=0, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=self.wrong_button_pressed)
        check_bt = tk.Button(master=frame, image=self.right_image, borderwidth=0, highlightthickness=0, activebackground=BACKGROUND_COLOR, command=self.check_button_pressed)
        view_bt = tk.Button(master=frame, image=self.view_image, borderwidth=0, highlightthickness=0,bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, command=self.view_button_pressed)
        wrong_bt.grid(row=0, column=0, padx=25), check_bt.grid(row=0 ,column=2, padx=25), view_bt.grid(row=0, column=1, padx=25)

    def random_data_row(self):
        if not self.db.empty:
            random_dex = randint(0, len(self.db) - 1)
            word, mean = self.db.loc[random_dex, ["English", "Meaning"]]  # index, column
            return word, mean

    def check_button_pressed(self):
        if not self.db.empty:
            used_word = self.get_the_word()
            word, _ = self.random_data_row()
            self.canvas.itemconfig(self.canvas_image, image=self.front_card)
            self.canvas.itemconfig(self.title_txt, text="ENGLISH", fill= "black")
            self.canvas.itemconfig(self.text_txt, text=formatted_text(21, word), fill="black", font=("Arial", 60, "bold"))

            if self.to_learn_on:
                row_index = self.db.index[self.db.English == used_word]
                self.db = self.db.drop(row_index)
                self.db = self.db.reset_index(drop=True)

                self.db.to_csv("words_to_learn.csv")
                if self.db.empty:
                    self.empty_words(self.front_card)
        else:
            self.empty_words(self.front_card)
    def wrong_button_pressed(self):
        if not self.db.empty:
            used_word = self.get_the_word()
            word, _ = self.random_data_row()
            self.canvas.itemconfig(self.canvas_image, image=self.front_card)
            self.canvas.itemconfig(self.title_txt, text="ENGLISH", fill= "black")
            self.canvas.itemconfig(self.text_txt, text=formatted_text(21, word), fill="black", font=("Arial", 60, "bold"))

            row_index = self.db.index[self.db.English == used_word]
            add_row = {"English": used_word, "Meaning": self.db.iloc[row_index, 1].values[0]}

            self.to_learn_db = pd.concat([self.to_learn_db, pd.DataFrame([add_row])], ignore_index=True)
            self.to_learn_db.to_csv("words_to_learn.csv")


    def view_button_pressed(self):
        if self.canvas.itemcget(self.title_txt, "text") in ("ENGLISH", "EMPTY"):
            mask = self.db[self.db["English"] == self.canvas.itemcget(self.text_txt, "text")]
            if not mask.empty:
                row = next(mask.itertuples(index=False), None)  # next move to the next term to be iterable
                word, mean = row.English, row.Meaning
                self.canvas.itemconfig(self.canvas_image, image=self.back_card)
                self.canvas.itemconfig(self.title_txt, text=word, fill="white")
                self.canvas.itemconfig(self.text_txt, text=formatted_text(50, mean), font=("Arial", 20, "bold"), fill="white")
            else:
                self.empty_words(self.back_card)

    def get_the_word(self):
        if self.canvas.itemcget(self.title_txt, "text") == "ENGLISH":
            return self.canvas.itemcget(self.text_txt, "text")
        else:
            return self.canvas.itemcget(self.title_txt, "text")

    def empty_words(self, card_image):
        self.canvas.itemconfig(self.canvas_image, image=card_image)
        self.canvas.itemconfig(self.title_txt, text="EMPTY")
        self.canvas.itemconfig(self.text_txt, text="")


def main():
    app = EnFlashCard()
    app.root.mainloop()


if __name__ == "__main__":
    main()