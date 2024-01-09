import tkinter as tk
FONT = ("Courier New", 13, "bold")
CONVERSION_FACTOR = 0.621371
convert_value = 0
def button_pressed():
    if entry.get().isnumeric():
        var = float(entry.get())
        label["text"] = round(var / CONVERSION_FACTOR, 2)

root = tk.Tk()
root.title("Mile to Kilometer")
root.geometry() ###
root.minsize() ###
root.config(padx=15, pady=15)

# Entry user_input
entry = tk.Entry(width=10)
entry.insert(tk.END, "0")
entry.grid(column=1, row=0)

# Labels texts
col_row = [(2, 0), (0, 1), (2,1), (1,1)]
label_txt = ["Mile", "is equal to", "Km", convert_value]
for position, text in zip(col_row, label_txt):
    x, y = position
    label = tk.Label(text=text, font=FONT)
    label.config(pady=10, padx=10)
    label.grid(column=x,row=y)


button = tk.Button(text="Convert", width=10, command=button_pressed)
button.config(padx=10, pady=10)
button.grid(row=2, column=1)

root.mainloop()