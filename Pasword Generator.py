import tkinter
from tkinter import *
import string
from tkinter import ttk
import random
import pyperclip
# **********************MAIN WINDOW**********************
root = Tk()
root.title("")
root.geometry("440x320+100+200")

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    length = int(ENTRY.get())
    selected_strength = strength.get()

    if selected_strength == "Weak":
        All = small_alphabets + capital_alphabets
    elif selected_strength == "Medium":
        All = small_alphabets + capital_alphabets + numbers
    elif selected_strength == "Strong":
        All = small_alphabets + capital_alphabets + numbers + special_characters
    else:
        All = small_alphabets + capital_alphabets + numbers + special_characters

    Password = random.choices(All, k=length)
    Password = ''.join(Password)
    Pasword_Field.delete(0, 'end')
    Pasword_Field.insert(0, Password)

def Copy():
    Copy=Pasword_Field.get()
    pyperclip.copy(Copy)

title_lbl = Label(root, text="PASSWORD GENERATOR", font=("Bradley Hand ITC", 25, "bold"), bg="rosybrown", fg="white")
title_lbl.place(x=0, y=0, width=440, height=45)

Length = Label(root, text="Length", font=("Freestyle Script", 35, "bold"), fg="teal")
Length.place(x=12, y=50, width=130, height=49)

ENTRY = Spinbox(root, highlightthickness=1, highlightbackground="black", font=("times new roman", 18), from_=5, to=18)
ENTRY.place(x=150, y=59, width=150, height=35)

Strength = Label(root, text="Strength", font=("Freestyle Script", 32, "bold"), fg="teal")
Strength.place(x=10, y=105, width=140, height=47)

strength = ttk.Combobox(root, font=("times new roman", 18))
strength["values"] = ("Select", "Weak","Medium", "Strong")
strength.current((0))
strength.place(x=150, y=110, width=150, height=35)

Generate_Button = Button(root, command=generator, text="Generate", font=("times new roman", 18), bg="olive", fg="white")
Generate_Button.place(x=120, y=160, width=200, height=35)

Pasword_Field = Entry(root,font=("times new roman", 18))
Pasword_Field.place(x=80, y=210, width=275, height=35)

Copy_Button = Button(root, command=Copy, text="Copy", font=("times new roman", 18), bg="olive", fg="white")
Copy_Button.place(x=120, y=260, width=200, height=35)

root.mainloop()













