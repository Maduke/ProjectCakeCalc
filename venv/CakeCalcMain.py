from tkinter import *
from tkinter import ttk

def _test_Input():
    sum = cakeSizeC5.get()+cakeSizeC6.get()+cakeSizeC7.get()+cakeSizeC8.get() + cakeSizeC9.get() + cakeSizeC10.get() + \
    cakeSizeC12.get() + cakeSizeC14.get() + cakeSizeC16.get() + cakeSizeS10.get() + cakeSizeS12.get() + \
    cakeSizeS14.get() + cakeSizeS16.get()

    print("Total Slices: " + str(sum))
    out1.delete(0, 'end')
    out1.insert(0, str(sum))


def show_roundCakes():  # show all round cake sizes
    clearWidg(f123)
    Checkbutton(f123, text='5-in', onvalue=7, variable=cakeSizeC5).grid(row=1, column=0)
    Checkbutton(f123, text='6-in', onvalue=9, variable=cakeSizeC6).grid(row=2, column=0)
    Checkbutton(f123, text='7-in', onvalue=12, variable=cakeSizeC7).grid(row=3, column=0)
    Checkbutton(f123, text='8-in', onvalue=16, variable=cakeSizeC8).grid(row=4, column=0)
    Checkbutton(f123, text='9-in', onvalue=21, variable=cakeSizeC9).grid(row=5, column=0)
    Checkbutton(f123, text='10-in', onvalue=27, variable=cakeSizeC10).grid(row=6, column=0)
    Checkbutton(f123, text='12-in', onvalue=34, variable=cakeSizeC12).grid(row=7, column=0)
    Checkbutton(f123, text='14-in', onvalue=50, variable=cakeSizeC14).grid(row=8, column=0)
    Checkbutton(f123, text='16-in', onvalue=60, variable=cakeSizeC16).grid(row=9, column=0)
    bC['relief'] = 'sunken'
    bS['relief'] = 'raised'
    #f123.update()
    print('Updated')


def show_squareCakes():  # show all square cake sizes
    clearWidg(f123)
    Checkbutton(f123, text='10-in', onvalue=26, variable=cakeSizeS10).grid(row=1, column=0)
    Checkbutton(f123, text='12-in', onvalue=40, variable=cakeSizeS12).grid(row=2, column=0)
    Checkbutton(f123, text='14-in', onvalue=60, variable=cakeSizeS14).grid(row=3, column=0)
    Checkbutton(f123, text='16-in', onvalue=90, variable=cakeSizeS16).grid(row=4, column=0)
    bS['relief'] = 'sunken'
    bC['relief'] = 'raised'
    #f123.update()
    print('Updated')


def clearWidg(fName):
    for widget in fName.winfo_children():
        widget.deselect()  # Uncheck all check buttons
        widget.destroy()  # Remove all widgets from the frame
    print('Cleared Widget')



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
#window.iconbitmap('BakeryLogo.png')
frame1 = Frame(window, relief="sunken")
frame1.grid(padx=100, pady=5, row=0, column=0)

# Show cake shape selector
f123 = Frame(frame1)
f123.grid(row=2, column=0)
bC = Button(frame1, text="Circular Cake", command=show_roundCakes)
bS = Button(frame1, text="Square Cake", command=show_squareCakes)
bC.grid(row=0, column=0)
bS.grid(row=0, column=1)
# Show 'cake size' label
Label(frame1, text='CakeSize').grid(row=1, column=0)

# show button and output
b1 = Button(frame1, text="Calculate", command=_test_Input)
b1.grid(row=6, column=0)
out1 = Entry(frame1, justify='center')
out1.grid(row=6, column=1)

# show step 2 options
frame2 = Frame(frame1)
frame2.grid(row=0, column=3)
Label(frame2, text="Step 2").grid(row=0, column=0)
ttk.Separator(frame2, orient=VERTICAL).grid(row=0, column=2, rowspan=3, sticky=(S,N))
window.mainloop()


# Example Program
# def evntCheck(event=None):
#     print(str(not(boolChk.get())))
#
#
# def evnt_Sub(event):
#     box1 = txtEntry.get()
#     if boolChk.get():
#         box1 = box1.upper()
#     txtOut.delete(0, "end")
#     txtOut.insert(0, box1)
#
#
# window = Tk()
#
# boolChk = BooleanVar()
# boolChk.set(False)
#
# window.title("Custom Creations Cake Calculator")
# mainFrame = Frame(window)
# mainFrame.grid(padx=200, pady=5)
#
# txtEntry = Entry(mainFrame)
# txtEntry.grid(row=0, column=0)
#
# checkbtn = Checkbutton(mainFrame, text="Upper", variable=boolChk)
# checkbtn.bind("<Button-1>", evntCheck)
# checkbtn.grid(row=1, column=0)
#
# txtOut = Entry(mainFrame)
# txtOut.grid(row=2, column=0)
#
# subBtn = Button(mainFrame, text="Submit")
# subBtn.grid(row=3, column=0)
# subBtn.bind("<Button-1>", evnt_Sub)
#
#
# window.mainloop()
