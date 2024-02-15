from tkinter import *
import requests

def get_quote():
    with requests.get(url="https://api.kanye.rest/") as response:
        response.raise_for_status()
        data = response.json()
        canvas.itemconfig(quote_text, text=data["quote"])
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="#90EE90")

canvas = Canvas(width=300, height=414, bg="#90EE90", highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Yo, what's good?", width=250, font=("Arial", 18, "bold"), fill="#FF6347")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="#90EE90", activebackground="#90EE90", border=0)
kanye_button.grid(row=1, column=0)



window.mainloop()