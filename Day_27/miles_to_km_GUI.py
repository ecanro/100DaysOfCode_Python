import tkinter

# miles to km function


def miles_to_km():
    miles = float(input_miles.get())
    km = round(miles) * 1.609
    label3.config(text=km)


# create the windows
windows = tkinter.Tk()
windows.title("Miles to Km converter")
windows.minsize(width=150, height=50)
windows.config(padx=40, pady=15)

# create input
input_miles = tkinter.Entry(width=20)
print(input_miles)
input_miles.grid(column=1, row=0)

# create labels
label1= tkinter.Label(text="Miles")
label1.grid(column=2, row=0)
label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)
label3 = tkinter.Label(text="0")
label3.grid(column=1, row=1)
label4 = tkinter.Label(text="Km")
label4.grid(column=3, row=1)

# create button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

windows.mainloop()