import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=YELLOW)




my_label = tkinter.Label(text="placeholder", font=("Arial",16,"bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=0, column=1)

my_button_know = tkinter.Button(text="✔", highlightthickness=0)
my_button_know.grid(row=1, column=0)

my_button_dontknow = tkinter.Button(text="✘", highlightthickness=0)
my_button_dontknow.grid(row=1, column=1)

canvas = tkinter.Canvas(width=800, height=524, bg=YELLOW, highlightthickness=0)


window.mainloop()
