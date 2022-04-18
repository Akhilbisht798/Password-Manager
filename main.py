from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genrate_password():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ['0','1','2','3','4','5','6','7','8','9']
    char = ['!','@','#','%','*']
    n_l = random.randint(6,10)
    n_n = random.randint(4,6)
    n_c = random.randint(3,4)
    pas = []
    for c in range(n_l):
        pas.append(random.choice(letter))
    for c in range(n_n):
        pas.append(random.choice(num))
    for c in range(n_c):
        pas.append(random.choice(char))

    random.shuffle(pas)
    password = ""
    for p in pas:
        password += p
    password_Entry.delete(0, END)
    password_Entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    user = username_Entry.get()
    pas = password_Entry.get()
    if (len(web) == 0 or len(user) == 0 or len(pas) == 0):
        messagebox.showinfo(title="Oops", message="you left something empty")
    else:
        ok = messagebox.askyesno(title=web, message=f"Please Confirm Your Detail\nEmail: {user}\nPassword: {pas}")
        if ok:
            with open("data.txt" , "a") as data_file:
                data_file.write(f"{web} | {user} | {pas}\n")
                web_entry.delete(0, END)
                password_Entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#canvas
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row = 0,column=1)

#Label
website_label = Label(text="Website:")
username_l = Label(text="Email/Username:")
password_l = Label(text="Password:")

website_label.grid(row=1,column=0)
username_l.grid(row=2,column=0)
password_l.grid(row=3,column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
username_Entry = Entry(width=35)
username_Entry.grid(row=2,column=1,columnspan=2)
password_Entry = Entry(width=21)
password_Entry.grid(row=3,column=1,columnspan=2)

#button
genrate_pass = Button(text="Create Password" ,command=genrate_password)
genrate_pass.grid(row=3, column=2)
add_button = Button(text="Add", width=36 ,command=save)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()