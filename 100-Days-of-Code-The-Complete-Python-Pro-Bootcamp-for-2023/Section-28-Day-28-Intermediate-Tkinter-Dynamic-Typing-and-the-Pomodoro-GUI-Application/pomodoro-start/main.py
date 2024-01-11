import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def button_reset_used():
    global reps
    root.after_cancel(timer)
    canvas.itemconfig(text_canvas, text="25:00")
    label_title.config(text="Timer")
    label_check.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def button_start_used():
    global reps
    print(reps)
    if reps % 2 == 0 :
        time = WORK_MIN * 60
        countdown(time)
        label_title.config(text="Work", fg=GREEN)
    elif reps % 4 == 0 and reps != 0:
        time = LONG_BREAK_MIN * 60
        countdown(time)
        label_title.config(text="Break", fg=RED)
    else:
        time = SHORT_BREAK_MIN * 60
        countdown(time)
        label_title.config(text="Break", fg=RED)
    reps += 1
    # countdown(time)
    # root.after(1000,button_reset_used)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min = [math.floor(count / 60), count % 60]
    if count_min[1] < 10:
        count_min[1] = "0" + str(count_min[1])
    canvas.itemconfig(tagOrId=text_canvas, text=f"{count_min[0]}:{count_min[1]:2}")
    if count > 0:
       timer = root.after(1000, countdown, count - 1)
    else:
        button_start_used()  # should've named it better
        check = ""
        for _ in range(math.floor(reps/2)):
            check += "️️✔️"

        label_check.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Pomodoro")
root.geometry()
root.minsize()
root.config(padx=100, pady=50, bg=YELLOW)



canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato= tk.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato)
text_canvas = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

# labels
label_title = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME,35, "bold"), bg=YELLOW, highlightthickness=0)
label_title.grid(row=0, column=1)

label_check = tk.Label( fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME,20, "bold"))
label_check.config(pady=10)
label_check.grid(row=2, column=1)

# Buttons
button_start = tk.Button(text="Start",width=5, bg=PINK, command=button_start_used, activebackground="pink", highlightthickness=0)
button_start.grid(row=2, column=0)

button_reset = tk.Button(text="Reset",width=5,  bg=PINK, command=button_reset_used, activebackground="pink", highlightthickness=0)
button_reset.grid(row=2,column=2)
root.mainloop()
