# Tkinter
import tkinter

# the windows
windows = tkinter.Tk()
windows.title("My First GUI Programs")
windows.minsize(width=480, height=480)
# adding padding
windows.config(padx=20, pady=20)

# labels-> first create component(widget)
my_label = tkinter.Label(text="my_label", font=("Arial", 24, "bold"))
my_label["text"] = "New text"#->or
my_label.config(text="Other text")#->other option
# adding padding
my_label.config(padx=20, pady=20)

# now create the pack->insert the component(widget) in the windows
#tkinter layout managers: pack(), place() and grid(), only choose one
# my_label.pack()#->when we use .pack() we use **kw-advance arguments, pack alocated all the widgets slaves in the master
# my_label.place(0, 0)#-> use x,y coordenates 0,0 is the left top corner

# the best way is use grid
my_label.grid(column=0, row=0)#->look he displayed in the same place because we not have another widget to located


# button
button = tkinter.Button(text="Click me", command="button_clicked")
button.grid(column=1, row=1)

# input
input = tkinter.Entry(width=20)
print(input.get())
input.grid(column=2, row=2)





windows.mainloop()