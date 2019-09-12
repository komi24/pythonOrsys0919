# -*- coding: utf-8 -*-

from tkinter import *
from time import sleep


fen = Tk()

i = 0
def update_canvas():
    global i
    canvas.delete('all')
    canvas.create_image(32+(i%5)*64,32+(i%5)*64,image=photo)
    i += 1
    canvas.after(1000, update_canvas)
    
    
canvas = Canvas(fen, width=600, height=600)
photo = PhotoImage(file='pomp.png')
canvas.pack()

update_canvas()

fen.mainloop()
