import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    my_entry_password.delete(0,100)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    my_entry_password.insert(0, password)
    pyperclip.copy(password)

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

def write_file():
    my_website = my_entry_website.get()
    my_username = my_entry_username.get()
    my_password = my_entry_password.get()
    new_data ={
        my_website: {
            "email": my_username,
            "password": my_password

        }
    }

    if my_website == "" or my_username == "" or my_password == "":
        messagebox.showinfo("Error", "Please fill all fields")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=my_website, message=f"You entered \nusername: {my_username}"
                                                                         f"\npassword: {my_password}\n Is it ok to save?")
        if is_ok:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
                
                my_entry_website.delete(0, 100)
                my_entry_password.delete(0, 100)

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
my_button_password = tkinter.Button(text="Generate Password", command=generate_password)
my_button_password.grid(row=3, column=2)
my_button_add = tkinter.Button(text="Add", width=36, command=write_file)
my_button_add.grid(row=4, column=1,columnspan=2)





window.mainloop()
