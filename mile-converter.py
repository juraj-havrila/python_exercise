import tkinter

window = tkinter.Tk()
window.title("Mile to km converter")
window.minsize(100, 50)
window.config(padx=20, pady=20)

my_label_miles_tag = tkinter.Label(text="miles", font=("Arial",10))
my_label_miles_tag.grid(column=2,row=0)
my_label_is_equal = tkinter.Label(text="is equal to", font=("Arial",10))
my_label_is_equal.grid(column=0,row=1)
my_label_km_tag = tkinter.Label(text="km", font=("Arial",10))
my_label_km_tag.grid(column=2,row=1)
my_label_km_value = tkinter.Label(text="..", font=("Arial",10,"bold"))
my_label_km_value.grid(column=1,row=1)

my_input=tkinter.Entry(width=10)
my_input.focus()
my_input.grid(column=1,row=0)

def button_clicked():
    print("Button Clicked")
    my_miles = int(my_input.get())
    my_km=my_miles*1.609
    my_label_km_value.config(text=f"{my_km}")

my_button = tkinter.Button(text="Calculate", command=button_clicked)
my_button.grid(column=1,row=2)


window.mainloop()