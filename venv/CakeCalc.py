from tkinter import *
from tkinter import ttk


def show_roundCakes():  # show all round cake sizes
    clearWidg(cakeListBox)
    Checkbutton(cakeListBox, text='5-in', onvalue=7, variable=cakeSizeC5).grid(row=1, column=0)
    Checkbutton(cakeListBox, text='6-in', onvalue=9, variable=cakeSizeC6).grid(row=2, column=0)
    Checkbutton(cakeListBox, text='7-in', onvalue=12, variable=cakeSizeC7).grid(row=3, column=0)
    Checkbutton(cakeListBox, text='8-in', onvalue=16, variable=cakeSizeC8).grid(row=4, column=0)
    Checkbutton(cakeListBox, text='9-in', onvalue=21, variable=cakeSizeC9).grid(row=5, column=0)
    Checkbutton(cakeListBox, text='10-in', onvalue=27, variable=cakeSizeC10).grid(row=6, column=0)
    Checkbutton(cakeListBox, text='12-in', onvalue=34, variable=cakeSizeC12).grid(row=7, column=0)
    Checkbutton(cakeListBox, text='14-in', onvalue=50, variable=cakeSizeC14).grid(row=8, column=0)
    Checkbutton(cakeListBox, text='16-in', onvalue=60, variable=cakeSizeC16).grid(row=9, column=0)
    bC['relief'] = 'sunken'
    bS['relief'] = 'raised'
    #cakeListBox.update()
    print('Updated')


def show_squareCakes():  # show all square cake sizes
    clearWidg(cakeListBox)
    Checkbutton(cakeListBox, text='10-in', onvalue=26, variable=cakeSizeS10).grid(row=1, column=0)
    Checkbutton(cakeListBox, text='12-in', onvalue=40, variable=cakeSizeS12).grid(row=2, column=0)
    Checkbutton(cakeListBox, text='14-in', onvalue=60, variable=cakeSizeS14).grid(row=3, column=0)
    Checkbutton(cakeListBox, text='16-in', onvalue=90, variable=cakeSizeS16).grid(row=4, column=0)
    bS['relief'] = 'sunken'
    bC['relief'] = 'raised'
    #cakeListBox.update()
    print('Updated')


def clearWidg(fName):
    for widget in fName.winfo_children():
        widget.deselect()  # Uncheck all check buttons
        widget.destroy()  # Remove all widgets from the frame
    print('Cleared Widget')


def show_S1():
    step2F.grid_forget()
    step1F.grid(row=0, column=3)
    step3F.grid_forget()

def show_S2():
    step1F.grid_forget()
    step2F.grid(row=0, column=6)
    step3F.grid_forget()


def show_S3():
    step1F.grid_forget()
    step2F.grid_forget()
    step3F.grid(row=0, column=9)


window = Tk()
# Variable declarations
cakeSizeS10 = IntVar()
cakeSizeS12 = IntVar()
cakeSizeS14 = IntVar()
cakeSizeS16 = IntVar()
cakeSizeC5 = IntVar()
cakeSizeC6 = IntVar()
cakeSizeC7 = IntVar()
cakeSizeC8 = IntVar()
cakeSizeC9 = IntVar()
cakeSizeC10 = IntVar()
cakeSizeC12 = IntVar()
cakeSizeC14 = IntVar()
cakeSizeC16 = IntVar()

# Set up the window with a name, icon and basic formatting
window.title("Custom Creations Cake Calculator")
# window.iconbitmap('BakeryLogo.png')
frame_main = Frame(window, relief="sunken")
frame_main.grid(padx=50, pady=5, row=0, column=0)

# Set up Step 1 button and seperator
st1B = Button(frame_main, text="Step 1", command=show_S1, bg='blue', activebackground='lightblue')
st1B.grid(row=0, column=0)
ttk.Separator(frame_main, orient=VERTICAL).grid(row=0, column=2, rowspan=3, padx=5, sticky=(S, N))

step1F = Frame(frame_main, bg='lightblue', padx=5, pady=5)
step1F.grid(row=0, column=3)

# Set up Cake Type Buttons
bC = Button(step1F, text="Circular Cake", command=show_roundCakes)
bS = Button(step1F, text="Square Cake", command=show_squareCakes)
bC.grid(row=0, column=0)
bS.grid(row=0, column=1)

# Set up box for the size options
cakeListBox = Frame(step1F)
cakeListBox.grid(row=1, column=0)

# Set up Step 2 button and seperator
st2B = Button(frame_main, text="Step 2", command=show_S2)
st2B.grid(row=0, column=4)
ttk.Separator(frame_main, orient=VERTICAL).grid(row=0, column=5, rowspan=3, padx=5, sticky=(S, N))

step2F = Frame(frame_main, padx=5, pady=5)
step2F.grid(row=0, column=6, padx=5, pady=5)

# Set up Step 3 button and seperator
st3B = Button(frame_main, text='Step 3', command=show_S3)
st3B.grid(row=0, column=7, padx=5, pady=5)
ttk.Separator(frame_main, orient=VERTICAL).grid(row=0, column=8, rowspan=3, padx=5, sticky=(S, N))

step3F = Frame(frame_main, padx=5, pady=5)
step3F.grid(row=0, column=9, padx=5, pady=5)

window.mainloop()
