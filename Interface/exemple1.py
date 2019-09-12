# -*- coding: utf-8 -*-

from tkinter import *
from itertools import product


fen = Tk()

label = Label(fen,
              text="Salut PSA",
              width=20,
              height=6)
label.pack(side=LEFT)

frame = Frame(fen)
frame.pack()

for i,j in product(range(3), range(3)):
    button = Button(frame, text="%d - %d"%(i,j))
    button.grid(row=i, column=j)

fen.mainloop()

