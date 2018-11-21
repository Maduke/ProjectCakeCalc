from tkinter import *
from tkinter import ttk


def test_mod():
    print("Cake Module Is Working")


def clearWidg(fName):
    for widget in fName.winfo_children():
        widget.deselect()  # Uncheck all check buttons
        widget.destroy()  # Remove all widgets from the frame
    print('Cleared Widget')


def show_S1(step1Frame, step2Frame, step3Frame, st1Menu):

    step1Frame.grid(row=0, column=0)
    step2Frame.grid_forget()
    step3Frame.grid_forget()
    st1Menu.grid(row=0, column=0)



def show_S2():
    step1Frame.grid_forget()
    step2Frame.grid(row=0, column=0)
    step3Frame.grid_forget()


def show_S3():
    step1Frame.grid_forget()
    step2Frame.grid_forget()
    step3Frame.grid(row=0, column=0)
