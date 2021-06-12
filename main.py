from tkinter import *
from tkinter import ttk


root = Tk()
root.title("user interface")
root.geometry('400x300')
root.configure(bg='light blue')

user_pass = {'Lerato': 'lerato@741'}



entry1 = Entry(root, width=23)
entry1.place(x=170, y=100)
lbluser = Label(root, text="Username: ")
lbluser.place(x=20, y=100)

lblpass = Label(root, text="Password: ")
lblpass.place(x=20, y=200)
entry2 = Entry(root, width=23)
entry2.place(x=170, y=200)


def exit():
    root.destroy()
exit_btn = Button(text = "Quit", command=exit)
exit_btn.place(x=300, y=250)

def verify():
    if user_pass is

verify_btn = Button(text="verify", command=verify)
verify_btn.place(x=170, y=250)



root.mainloop()
