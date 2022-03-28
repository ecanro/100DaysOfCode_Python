from tkinter import * # only import class
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for n in range(nr_letters)]
    password_symbols = [random.choice(symbols) for n in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for n in range(nr_numbers)]

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json", mode="r") as data_find:
            data = json.load(data_find)
    except FileNotFoundError:
        messagebox.showwarning(title="Info:", message="No Data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"User_email: {email}\n" f"Password: {password}")
        else:
            messagebox.showinfo(title="Info:", message="Not details for the website exists!")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    user_email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": user_email,
            "password": password
        }
    }

    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showerror("Error", message="Please entry all fields")
    else:
        save_ok = messagebox.askokcancel(title=website, message=f"Register entered: \nEmail: {user_email}\n"
                                                     f"Password: {password}\nit's ok?")
        if save_ok:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", mode="w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                clean_inputs()


def clean_inputs():
    website_input.delete(0, END)
    website_input.focus()
    # email_username_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Manager")
windows.config(padx=50, pady=50)


# create canvas
canvas = Canvas(width=200, height=200)

logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# inputs
website_input = Entry(width=30)
# website_input.insert(END, string="insert the web site")
website_input.focus()
website_input.grid(column=1, row=1)

email_username_input = Entry(width=48)
email_username_input.insert(END, string="my_mail@mail.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=30)
password_input.grid(column=1, row=3)

# buttons
search_button = Button(width=12, text="Buscar", command=find_password)
search_button.grid(column=2, row=1)

password_generate_button = Button(text="Generar Password", command=gen_password)
password_generate_button.grid(column=2, row=3)

add_register_button = Button(width=41, text="Agregar", command=save)
add_register_button.grid(column=1, row=4, columnspan=2)


windows.mainloop()
