from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
start_clicked = False
timer = None
mark = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global mark, reps, start_clicked
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    text.config(text="Timer", fg=GREEN)
    mark = ""
    checkmark.config(text=mark)
    reps = 0
    start_clicked = False
    #timer_text 00:00
    #title_label "Timer"
    #reset check_marks

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, start_clicked

    if start_clicked:
        return
    start_clicked = True

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 1st/3rd/5th/7th rep:

    # if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        text.config(text="Break", fg=PINK)
    #If it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        text.config(text="Break", fg=RED)
        count_down(short_break_sec)
    else:
        text.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global start_clicked, mark
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_clicked = False
        start_timer()
        if math.floor(reps) % 2 == 0:
            mark += "✔"
            checkmark.config(text=mark)
            window.focus_force()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
text.grid(column=1, row=0)

start = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
start.grid(column=0, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
