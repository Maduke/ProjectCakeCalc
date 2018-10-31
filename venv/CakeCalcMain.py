from tkinter import *


def evntCheck(event=None):
    print(str(not(boolChk.get())))


def evnt_Sub(event):
    box1 = txtEntry.get()
    if boolChk.get():
        box1 = box1.upper()
    txtOut.delete(0, "end")
    txtOut.insert(0, box1)


window = Tk()

boolChk = BooleanVar()
boolChk.set(False)

window.title("Custom Creations Cake Calculator")
mainFrame = Frame(window)
mainFrame.grid(padx=200, pady=5)

txtEntry = Entry(mainFrame)
txtEntry.grid(row=0, column=0)

checkbtn = Checkbutton(mainFrame, text="Upper", variable=boolChk)
checkbtn.bind("<Button-1>", evntCheck)
checkbtn.grid(row=1, column=0)

txtOut = Entry(mainFrame)
txtOut.grid(row=2, column=0)

subBtn = Button(mainFrame, text="Submit")
subBtn.grid(row=3, column=0)
subBtn.bind("<Button-1>", evnt_Sub)


window.mainloop()
