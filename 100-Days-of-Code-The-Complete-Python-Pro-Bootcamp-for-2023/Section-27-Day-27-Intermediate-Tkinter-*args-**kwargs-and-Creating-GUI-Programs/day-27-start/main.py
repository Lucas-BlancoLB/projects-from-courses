import tkinter as tk

# creating a window and configurations
window = tk.Tk()
window.title("Widget | GUI program")
window.minsize(width=500, height=300)

# Labels

my_label = tk.Label(text="I Am a Label", font=("Arial", 28, "bold"))
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.pack()


# Button

def button_clicked():
    # Action
    print("I got clicked")
    my_label.config(text=entry.get())


button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
# it's a text input
entry = tk.Entry(width=30)
entry.pack()

# add some text to the Entry as preview text
# tk.END or END if * , is a constant defined in tkinter used as index
entry.insert(tk.END, string="some text here")
print(entry.get())  # gets the input

# Text
text = tk.Text(height=5, width=30)
text.focus()  # the cursor is the focus so it puts it there
text.insert(tk.END, "put some text here")
print(text.get("1.0", tk.END))  # "1.0" its start line.character
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = tk.Scale(from_=0, to=100, width=10, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    if checked_state.get() == 1:
        print("Checkbutton is checked.")
    else:
        print("Checkbutton is unchecked.")


checked_state = tk.IntVar()  # useful to do something cuz it's associated with Checkbutton with a variable=
checkbutton = tk.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print("button:", radio_state.get())


radio_state = tk.IntVar()
radio_button1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack(), radio_button2.pack()


#Listbox
def listbox_used(event):  # event is linked with <ListboxSelect>>
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tk.Listbox(height=4)
fruits = ["Apple","Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", func=listbox_used)  #<<ListboxSelect>> linked with event in func=listbox_used
listbox.pack()
window.mainloop()
