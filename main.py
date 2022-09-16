from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from json import *

# ---------------------------- DATABASE SEARCH ------------------------------- #
def search():
    ws = entry_website.get()
    try:
        with open("data.json", "r") as f:
            data = load(f)
            detail = data[ws]
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found.")
    except KeyError:
        messagebox.showinfo(title="Oops", message="No details for this website.")
    else:
        email = detail["email"]
        password = detail["password"]
        messagebox.showinfo(title=ws, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    r_letters = [random.choice(letters) for char in range(nr_letters)]
    r_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    r_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = r_letters + r_symbols + r_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    ws = entry_website.get()
    um = entry_email.get()
    pw = entry_password.get()
    new_data = {
        ws: {
            "email": um,
            "password": pw,
        }
    }

    if len(ws) == 0 or len(um) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Oops", message="Please fill the blank.")
    else:
        try:
            with open("data.json", "r") as f:
                data = load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                dump(data, f, indent=4)

        entry_website.delete(0, END)
        entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
p = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=p)
canvas.grid(column=1, row=0)

lable_1 = Label(text="Website:")
lable_1.grid(column=0, row=1)

lable_2 = Label(text="Email/ Username:")
lable_2.grid(column=0, row=2)

lable_3 = Label(text="Password:")
lable_3.grid(column=0, row=3)

entry_website = Entry(width=21)
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email.insert(END, "abc@gmail.com")

entry_password= Entry(width=21)
entry_password.grid(column=1, row=3, sticky="EW")

button_add = Button(text="Add", command=add, width=34)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

button_generate = Button(text="Generate Password", command=generate)
button_generate.grid(column=2, row=3)

button_search = Button(text="Search", width=15, command=search)
button_search.grid(column=2, row=1)

window.mainloop()