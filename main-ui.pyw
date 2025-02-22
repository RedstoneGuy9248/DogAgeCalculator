from tkinter import *
import datetime
import math
import os
import pickle

root = Tk()
root.title("Dog Age From D.O.B")
root.configure(bg="#222222")



def error_future():
    for widget in root.winfo_children():
        widget.destroy()
    ErrorFutureLabel = Label(root, text="Error: DOB is in the future!", bg="#222222", fg="#F0F4F8", font="Inter")
    ErrorFutureButton = Button(root, text="Back to DOB Enter Screen", command=get_dob, bg="#616E7C", fg="#F0F4F8", font="Inter")
    ErrorFutureLabel.pack()
    ErrorFutureButton.pack()

def error_invalid():
    for widget in root.winfo_children():
        widget.destroy()
    ErrorInvalidLabel = Label(root, text="Error:Invalid DOB! Please enter DOB in the format DD/MM/YYYY!", bg="#222222", fg="#F0F4F8", font="Inter")
    ErrorInvalidButton = Button(root, text="Back to DOB Enter Screen", command=get_dob, bg="#616E7C", fg="#F0F4F8", font="Inter")
    ErrorInvalidLabel.pack()
    ErrorInvalidButton.pack()

def getAge(d):
    if (d > 365.25):
        dy = 15
        y = 1
        d -= 365.25

    if (d > 365.25):
        dy += 9
        y = 2
        d -= 365.25

    while (d > 365.25):
        dy += 4
        y += 1
        d -= 365.25

    m = int(d / (365.25 / 12))

    if (y == 0):
        dm = float(m * 15)
    elif (y == 1):
        dm = float(m * 9)
    elif (y > 1):
        dm = float(m * 4)

    if (dm > 12):
        dy = dy + (dm // 12)
        dm = dm % 12

    dm = int(dm)
    dy = int(dy)
    global dogmonthstr
    global dogyearstr
    dogyearstr = str("{} Dog Years".format(dy))
    dogmonthstr = str("{} Dog Months".format(dm))

def print_dob():
    for widget in root.winfo_children():
        widget.destroy()
    today = datetime.datetime.today()

    d = (today - dob).days
    getAge(d)
    ylabel = Label(root, text=dogyearstr, bg="#222222", fg="#F0F4F8", font="Inter")
    mlabel = Label(root, text=dogmonthstr, bg="#222222", fg="#F0F4F8", font="Inter")
    rgcredit = Label(root, text="Made By @RedstoneGuy9248 (github)", bg="#222222", fg="#F0F4F8",
                     font="Inter")
    ylabel.pack()
    mlabel.pack()
    rgcredit.pack()
def get_dob2():
    global dob
    today = datetime.datetime.today()
    try:
        dobstr = enternewentry.get()
        dob = datetime.datetime.strptime(dobstr, "%d/%m/%Y")
        if dob > today:
            error_future()
        else:
            print_dob()
    except ValueError:
        error_invalid()

def get_dob():
    for widget in root.winfo_children():
        widget.destroy()
    global enternewentry
    enternewlabel = Label(root, text="Enter D.O.B (DD/MM/YYYY)", bg="#222222", fg="#F0F4F8", font="Inter")
    enternewentry = Entry(root, bg="#323F4B", font="Inter", fg="#FFFFFF")
    enternewbutton = Button(root, text="Submit", command=get_dob2, bg="#616E7C", fg="#F0F4F8", font="Inter")
    rgcredit = Label(root, text="Made By @RedstoneGuy9248 (github)", bg="#222222", fg="#F0F4F8",
                     font="Inter")
    enternewlabel.pack()
    enternewentry.pack()
    enternewbutton.pack()
    rgcredit.pack()

get_dob()


root.mainloop()