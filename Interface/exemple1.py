# -*- coding: utf-8 -*-

from tkinter import *
from itertools import product


fen = Tk()

label = Label(fen, text="0", height=2)
label.pack(side=TOP, expand=True, fill='both')

button_valider = Button(fen, text="Valider", height=2)
button_valider.pack(
        side=BOTTOM,
        expand=True,
        fill='both')

frame_op = Frame(fen)
frame_op.pack(side=RIGHT)

button_zero = Button(fen, text="0", height=2)
button_zero.pack(
        side=BOTTOM,
        expand=True,
        fill='both')

frame_number = Frame(fen)
frame_number.pack()

for op in ['+','-','*','/']:
    Button(frame_op, text=op, width=5, height=2).pack()

for i,j in product(range(3), range(3)):
    button = Button(frame_number, text="%d"%(3*(2-i)+j+1), width=5, height=2)
    button.grid(row=i, column=j)

fen.mainloop()

