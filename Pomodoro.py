from tkinter import *
"✔"
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Aries"
COURIER = "courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(text, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label.config(text="Break", fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        new_mark = ""
        for _ in range(reps//2):
            new_mark += "✔"
        check_marks.config(text=new_mark)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()


window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", fg=GREEN, font=(COURIER, 50, "bold"), bg=YELLOW, highlightthickness=0)
label.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=3, row=3)

check_marks = Label(text="", fg=GREEN, font=(FONT_NAME, 24), bg=YELLOW, highlightthickness=0)
check_marks.grid(column=1, row=4)

window.mainloop()
