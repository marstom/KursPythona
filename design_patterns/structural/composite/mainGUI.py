"""

Image editor
"""

# python application to create a simple button

import tkinter as tk


def hey():
    print("HEy")


top = tk.Tk()

top.geometry("500x400")

b = tk.Button(top, text="Simple", command=hey)
c = tk.Canvas(top, bg='pink', height=200)
arc = c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="white")
c.create_rectangle([10, 10, 23, 34])

b.pack()
c.pack()

top.mainloop()
