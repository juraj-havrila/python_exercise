import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file="logo.png")
#canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0, background="white")
canvas.create_image(100, 100, image=img )
#canvas.pack()
canvas.grid(row=0, column=1)

my_label_website = tkinter.Label(text="Website:")
my_label_website.grid(row=1, column=0)
my_label_username = tkinter.Label(text="Email/Username:")
my_label_username.grid(row=2, column=0)
my_label_password = tkinter.Label(text="Password:")
my_label_password.grid(row=3, column=0)

my_entry_website = tkinter.Entry(width=35)
my_entry_website.grid(row=1, column=1, columnspan=2)
my_entry_website.focus()
my_entry_username = tkinter.Entry(width=35)
my_entry_username.insert(0, "juraj@email.com")
my_entry_username.grid(row=2, column=1, columnspan=2)
my_entry_password = tkinter.Entry(width=21)
my_entry_password.grid(row=3, column=1)
my_button_password = tkinter.Button(text="Generate Password")
my_button_password.grid(row=3, column=2)
my_button_add = tkinter.Button(text="Add", width=36)
my_button_add.grid(row=4, column=1,columnspan=2)

window.mainloop()
