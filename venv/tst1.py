from tkinter import *
from tkinter import ttk
#from CakeModule import *


def clearWidg(fName):
    for widget in fName.winfo_children():
        widget.deselect()  # Uncheck all check buttons
        widget.destroy()  # Remove all widgets from the frame
    print('Cleared Widget')


def show_S1():
    step1Frame.grid(row=0, column=0)
    step2Frame.grid_forget()
    step3Frame.grid_forget()
    step1MenuFrame.grid(row=0, column=0)



def show_S2():
    step1Frame.grid_forget()
    step2Frame.grid(row=0, column=0)
    step3Frame.grid_forget()


def show_S3():
    step1Frame.grid_forget()
    step2Frame.grid_forget()
    step3Frame.grid(row=0, column=0)


def show_roundCakes():  # show all round cake sizes
    clearWidg(cakeSizeFrame)
    Checkbutton(cakeSizeFrame, text='5-in', onvalue=7, variable=cakeSizeC5).grid(row=1, column=0)
    Checkbutton(cakeSizeFrame, text='6-in', onvalue=9, variable=cakeSizeC6).grid(row=2, column=0)
    Checkbutton(cakeSizeFrame, text='7-in', onvalue=12, variable=cakeSizeC7).grid(row=3, column=0)
    Checkbutton(cakeSizeFrame, text='8-in', onvalue=16, variable=cakeSizeC8).grid(row=4, column=0)
    Checkbutton(cakeSizeFrame, text='9-in', onvalue=21, variable=cakeSizeC9).grid(row=5, column=0)
    Checkbutton(cakeSizeFrame, text='10-in', onvalue=27, variable=cakeSizeC10).grid(row=6, column=0)
    Checkbutton(cakeSizeFrame, text='12-in', onvalue=34, variable=cakeSizeC12).grid(row=7, column=0)
    Checkbutton(cakeSizeFrame, text='14-in', onvalue=50, variable=cakeSizeC14).grid(row=8, column=0)
    Checkbutton(cakeSizeFrame, text='16-in', onvalue=60, variable=cakeSizeC16).grid(row=9, column=0)
    bC['relief'] = 'sunken'
    bS['relief'] = 'raised'
    #cakeSizeFrame.update()
    print('Updated')


def show_squareCakes():  # show all square cake sizes
    clearWidg(cakeSizeFrame)
    Checkbutton(cakeSizeFrame, text='10-in', onvalue=26, variable=cakeSizeS10).grid(row=1, column=0)
    Checkbutton(cakeSizeFrame, text='12-in', onvalue=40, variable=cakeSizeS12).grid(row=2, column=0)
    Checkbutton(cakeSizeFrame, text='14-in', onvalue=60, variable=cakeSizeS14).grid(row=3, column=0)
    Checkbutton(cakeSizeFrame, text='16-in', onvalue=90, variable=cakeSizeS16).grid(row=4, column=0)
    bS['relief'] = 'sunken'
    bC['relief'] = 'raised'
    #cakeSizeFrame.update()
    print('Updated')


window = Tk()
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
cakeType = DoubleVar()
cakeTypeMod = DoubleVar()
sculpted = DoubleVar()
complexity = DoubleVar()

# Create the 3 main frames that define the formatting of the GUI
menuFrame = Frame(window)
menuFrame.grid(row=0, column=0)

bodyFrame = Frame(window)
bodyFrame.grid(row=1, column=0)

resultsFrame = Frame(window)
resultsFrame.grid(row=2, column=0)



# Set up the results bar
Button(resultsFrame, text="Calculate").grid(row=0, column=0)
resultsBox = Entry(resultsFrame).grid(row=0, column=1)

# Set up the main body
step1Frame = Frame(bodyFrame)
step2Frame = Frame(bodyFrame)
step3Frame = Frame(bodyFrame)
step1MenuFrame = Frame(step1Frame)
cakeSizeFrame = Frame(step1Frame)

# Set up step 2
Radiobutton(step2Frame, text="Normal", variable=cakeType, value=3.55).grid(row=0, column=0)
Label(step2Frame, text=" OR ").grid(row=0, column=1)
Radiobutton(step2Frame, text="Tiered", variable=cakeType, value=3.30).grid(row=0, column=2)
Checkbutton(step2Frame, text="Fondant Covered", onvalue=0.75, variable=cakeTypeMod).grid(row=1, column=0)
Checkbutton(step2Frame, text="Sculpted", onvalue=25.00, variable=sculpted).grid(row=2, column=0)

# set up step 3
Radiobutton(step2Frame, text="Simple", value=10.00, variable=complexity).grid(row=0, column=0)
Radiobutton(step2Frame, text="Medium", value=10.00, variable=complexity).grid(row=0, column=0)
Radiobutton(step2Frame, text="Hard", value=10.00, variable=complexity).grid(row=0, column=0)
Radiobutton(step2Frame, text="Complex", value=10.00, variable=complexity).grid(row=0, column=0)

# make step 1 visible from the start
show_S1()


# Set up the menu bar
st1Button = Button(menuFrame, text='Cake Size (Step 1)', command=show_S1)
st2Button = Button(menuFrame, text='Cake Type (Step 2)', command=show_S2)
st3Button = Button(menuFrame, text='Step 3', command=show_S3)
st1Button.grid(row=0, column=0)
st2Button.grid(row=0, column=1)
st3Button.grid(row=0, column=2)

# Set up Cake Type Buttons
bC = Button(step1MenuFrame, text="Circular Cake", command=show_roundCakes)
bS = Button(step1MenuFrame, text="Square Cake", command=show_squareCakes)
bC.grid(row=0, column=0)
bS.grid(row=0, column=1)
cakeSizeFrame.grid(row=1, column=0)

window.mainloop()
