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
reps=0
num_checks=0
my_timer = None
is_running = False
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, num_checks, my_timer, is_running
    is_running = False
    reps=0
    num_checks=0
    window.after_cancel(my_timer)
    my_label.config(text="⏰", font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    my_checkmark.config(text=num_checks * "✔", font=("Arial", 16, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, num_checks, is_running
    if is_running:
        return
    is_running = True
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        my_label.config(text="Break", font=("Arial", 24, "bold"), fg=RED, bg=YELLOW)
        count_down(long_break_sec)
        num_checks = 0
    elif reps % 2 == 0 and reps !=8:
        my_label.config(text="Break", font=("Arial", 24, "bold"), fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
        num_checks += 1
    else:
        count_down(work_sec)
        my_label.config(text="Work", font=("Arial", 24, "bold"), fg=GREEN, bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global my_timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        my_timer = window.after(1000,count_down, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




my_label = tkinter.Label(text="Pomodoro ⏰", font=("Arial",24,"bold"), fg=GREEN, bg=YELLOW)
my_label.grid(row=0, column=1)
my_checkmark = tkinter.Label(text=num_checks*"✔", font=("Arial",16,"bold"), fg=GREEN, bg=YELLOW)
my_checkmark.grid(row=3, column=1)
my_button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
my_button_start.grid(row=4, column=1)
my_button_start.grid(row=2, column=0)
my_button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
my_button_reset.grid(row=2, column=2)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=("DSEG",35, "bold"))
canvas.grid(row=1, column=1)




window.mainloop()
