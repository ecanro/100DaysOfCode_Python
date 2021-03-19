from tkinter import * # only import class
from tkinter import messagebox
import random
import pyperclip

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
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    user_email = email_username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showerror("Error", message="Please entry all fields")
    else:
        save_ok = messagebox.askokcancel(title=website, message=f"Register entered: \nEmail: {user_email}\n"
                                                            f"Password: {password}\nit's ok?")
        if save_ok:
            with open(f"data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {user_email} | {password} \n")
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
website_input = Entry(width=50)
# website_input.insert(END, string="insert the web site")
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_username_input = Entry(width=50)
email_username_input.insert(END, string="my_mail@mail.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

# buttons
password_generate_button = Button(text="Generate Password", command=gen_password)
password_generate_button.grid(column=2, row=3)

add_register_button = Button(width="42", text="Add", command=save)
add_register_button.grid(column=1, row=4, columnspan=2)


windows.mainloop()
