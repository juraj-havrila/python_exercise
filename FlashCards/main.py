import tkinter
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#b1ddc6"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
# ---------------------------- DATA SETUP ------------------------------- #

current_card = {}
to_learn = {}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
else:
    to_learn = data.to_dict(orient='records')

#word_list = data["french_word"].to_list()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word, fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400,150,text="Title", font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="Word", font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = tkinter.PhotoImage(file="images/right.png")
know_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)

#my_label = tkinter.Label(text="placeholder", font=("Arial",16,"bold"), fg=GREEN, bg=YELLOW)
#my_label.grid(row=0, column=1)
#my_button_know = tkinter.Button(text="✔", padx=30, highlightthickness=0)
#my_button_know.grid(row=1, column=0)
#my_button_dontknow = tkinter.Button(text="✘", padx=30, highlightthickness=0)
#my_button_dontknow.grid(row=1, column=1)


next_card()

window.mainloop()
