
import tkinter as tk

window = tk.Tk()
window.title("Custom Creations Cake Calculator")
mainFrame = tk.Frame(window)
mainFrame.grid(padx=200, pady=5)

tk.Label(mainFrame, text="Hello World").grid(row=0, column=0)
entry1 = tk.Entry(mainFrame, text='nothing')
entry1.grid(row=1, column=1)
tk.Label(mainFrame, text="Hello World").grid(row=1, column=0)
tk.Label(mainFrame, text="Hello World").grid(row=2, column=0)
tk.Label(mainFrame, text="Hello World").grid(row=3, column=0)
tk.Label(mainFrame, text="Hello World").grid(row=4, column=0)


tk.mainloop()