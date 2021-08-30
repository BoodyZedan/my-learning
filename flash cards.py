from tkinter import *
import pandas
from random import *

current_word = {}

DataFrame = pandas.read_csv("french_words.csv")

to_learn = DataFrame.to_dict(orient="records")
BACKGROUND_COLOR = "#B1DDC6"


def wrong():
    global current_word
    canvas.itemconfig(Title, text="French", fill="black")
    current_word = choice(to_learn)
    canvas.itemconfig(word, text=current_word["French"], fill="black")
    canvas.itemconfig(card, image=card_front)
    window.after(3000, func=flip_card)


def flip_card():
    global current_word
    canvas.itemconfig(Title, text="English", fill="white")
    canvas.itemconfig(word, text=current_word["English"], fill="white")
    canvas.itemconfig(card, image=card_back)

# ---------------------------------UI SETUP---------------------------------------- #


window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0, command=wrong())
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=0)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(width=800, height=526, file="card_back.png")
card_front = PhotoImage(width=800, height=526, file="card_front.png")
card = canvas.create_image(400, 263, image=card_front)
Title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong()


window.mainloop()
