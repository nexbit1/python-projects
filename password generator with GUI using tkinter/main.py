from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)    # saves to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo( message='PLEASE ENTER THE REQUIRED DATA')
    else:
        is_ok = messagebox.askokcancel(message=f'You\'re details entered are:\n Website: {website_data} '
                                               f'\nEmail: {email_data}'f'\nPassword: {password_data}')
        if is_ok:
            with open('data.txt', mode= 'a') as data:
                data.write(f'{website_data} | {email_data} | {password_data}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
x = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=x)
canvas.grid(row=0,column=1)

#WEBSITE LABEL
website_label = Label(text='Website: ')
website_label.grid(row=1,column=0)

#WEBSITE ENTRY
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1,column=1, columnspan=2)

#email/username label
username_label = Label(text='Username/Email: ')
username_label.grid(row=2,column=0)

#email entry
email_entry = Entry(width=35)
email_entry.insert(0,'youreverydayemail@gmail.com')
email_entry.grid(row=2,column=1,columnspan=2)

#password label
password_label = Label(text='Password: ')
password_label.grid(row=3, column=0)
#password_entry
password_entry = Entry(width=22)
password_entry.grid(row=3,column=1)

#generate button
generate_button = Button(text='Generate', command=generate)
generate_button.grid(row=3,column=2)

#add button
add_button = Button(text='Add',width=35,command = save)
add_button.grid(row=4, column=1,columnspan=2)

window.mainloop()