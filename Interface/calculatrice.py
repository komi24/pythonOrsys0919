# -*- coding: utf-8 -*-

from tkinter import *
from itertools import product


class OpButton(Button):
    def __init__(self, *args, **kwargs):
#        kwargs['command'] = self.print_op
        Button.__init__(self, *args, **kwargs)
        self.operator = kwargs['text']
    
    def print_op(self):
        print('op', self.operator)

class NumberButton(Button):
    def __init__(self, *args, **kwargs):
#        kwargs['command'] = self.print_number
        Button.__init__(self, *args, **kwargs)
        self.value = kwargs['text']
    
    def print_number(self):
        print('number', self.value)

#def valider():
#    print("Validation")
#
#def valider_bind(e):
#    print("Validation", e.widget)
#
#def print_op(e):
#    print("Op", e.widget.operator)

class Calculatrice:
    def __init__(self):
        self.fen = Tk()
        
        self.value = StringVar()
        self.value.set("0")
        self.label = Label(self.fen, textvariable=self.value, height=2)
        self.label.pack(side=TOP, expand=True, fill='both')    
    
        self.button_valider = Button(self.fen, text="Valider", height=2) #, command=valider)
        #button_valider.bind('<Button-1>', valider_bind)
        self.button_valider.pack(
                side=BOTTOM,
                expand=True,
                fill='both')
        
        self.frame_op = Frame(self.fen)
        self.frame_op.pack(side=RIGHT)
        
        self.button_zero = NumberButton(self.fen, text="0", height=2)
        self.button_zero.pack(
                side=BOTTOM,
                expand=True,
                fill='both')
        self.button_zero.bind('<Button-1>', self.handle_number)
        
        self.frame_number = Frame(self.fen)
        self.frame_number.pack()
        
        for op in ['+','-','*','/']:
            btn = OpButton(self.frame_op, text=op, width=5, height=2)
            btn.pack()
            btn.bind('<Button-1>', self.handle_op)
        #    btn.bind('<Button-1>', print_op)
        
        for i,j in product(range(3), range(3)):
            button = NumberButton(self.frame_number, text="%d"%(3*(2-i)+j+1), width=5, height=2)
            button.grid(row=i, column=j)
            button.bind('<Button-1>', self.handle_number)
        
        self.fen.mainloop()
    
    def handle_number(self, e):
        self.value.set(e.widget.value)
    
    def handle_op(self, e):
        self.value.set(e.widget.operator)
    
calc = Calculatrice()