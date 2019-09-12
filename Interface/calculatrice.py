# -*- coding: utf-8 -*-
from tkinter import *
from itertools import product


class OpButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.operator = kwargs['text']
    

class NumberButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.value = kwargs['text']
    
    def print_number(self):
        print('number', self.value)


class Calculatrice:
    def __init__(self):
        self.fen = Tk()
        
        self.operand_1 = 0
        self.operand_2 = 0
        self.operator= '+'
        
        self.value = StringVar()
        self.value.set("")
        self.label = Label(self.fen, textvariable=self.value, height=2)
        self.label.pack(side=TOP, expand=True, fill='both')    
    
        self.button_valider = Button(self.fen, text="Valider", height=2) #, command=valider)
        self.button_valider.bind('<Button-1>', self.handle_validate)
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
        curr_operand = self.value.get() + e.widget.value
        self.value.set(curr_operand)
        self.operand_2 = int(curr_operand)
    
    def handle_op(self, e):
        if self.operator == '+':
            self.operand_1 += self.operand_2
        if self.operator == '-':
            self.operand_1 -= self.operand_2
        if self.operator == '*':
            self.operand_1 *= self.operand_2
        if self.operator == '/':
            self.operand_1 /= self.operand_2
        self.operand_2 = 0
        self.value.set('')
        self.operator = e.widget.operator
        
    def handle_validate(self, e):
        if self.operator == '+':
            self.operand_1 += self.operand_2
        if self.operator == '-':
            self.operand_1 -= self.operand_2
        if self.operator == '*':
            self.operand_1 *= self.operand_2
        if self.operator == '/':
            self.operand_1 /= self.operand_2
        self.operand_2 = 0
        self.value.set(str(self.operand_1))
    
calc = Calculatrice()