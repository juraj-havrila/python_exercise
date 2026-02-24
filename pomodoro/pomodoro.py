import tkinter
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000,count_down, count -1)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




my_label = tkinter.Label(text="Pomodoro ⏰", font=("Arial",24,"bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=0, column=1)
my_checkmark = tkinter.Label(text=3*"✔", font=("Arial",16,"bold"), fg=GREEN, bg=YELLOW)
my_checkmark.grid(row=3, column=1)
my_button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
my_button_start.grid(row=4, column=1)
my_button_start.grid(row=2, column=0)
my_button_reset = tkinter.Button(text="Reset", highlightthickness=0)
my_button_reset.grid(row=2, column=2)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=("DSEG",35, "bold"))
canvas.grid(row=1, column=1)




window.mainloop()
