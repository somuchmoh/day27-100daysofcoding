import tkinter

window = tkinter.Tk()
window.title("Mile to km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

# Input
text_input = tkinter.Entry(width=10)
text_input.grid(row=1, column=2)


# Label (miles)
miles_label = tkinter.Label(text="miles", font=("Arial", 14, "normal"))
miles_label.grid(row=1, column=3)

# Label (is equal to)
equal_label = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
equal_label.grid(row=2, column=1)

# Label (conversion)
label = tkinter.Label(text="0", font=("Arial", 14, "normal"))
label.grid(row=2, column=2)

# Label (km)
km_label = tkinter.Label(text="km", font=("Arial", 14, "normal"))
km_label.grid(row=2, column=3)


def button_click():
    miles = text_input.get()
    km = round(int(miles) * 1.609)
    label.config(text=f"{km}")


# Button
button = tkinter.Button(text="Calculate", command=button_click)
button.grid(row=3, column=2)

window.mainloop()
