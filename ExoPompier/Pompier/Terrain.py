# -*- coding: utf-8 -*-
from .Pompier import Pompier
from .Feu import Feu
import numpy as np
from tkinter import *


def dist(feu, pompier):
    return np.linalg.norm(feu.position - pompier.position)


class Terrain:
    def __init__(self):
        self.fen = Tk()
        self.canvas = Canvas(self.fen, width=704, height=704)
        self.photo_pompier = PhotoImage(file='pomp.png')
        self.photo_feu = PhotoImage(file='feu.gif')
        self.canvas.pack()
                
        self.liste_pompiers = [Pompier(self) for i in range(3)]
        self.liste_feux = [Feu() for i in range(10)]
    
    def update_canvas(self):
        self.canvas.delete('all')
        for pompier in self.liste_pompiers:
            self.canvas.create_image(
                    32+pompier.position[0]*64,
                    32+pompier.position[1]*64,
                    image=self.photo_pompier
                    )
        for feu in self.liste_feux:
            self.canvas.create_image(
                    32+feu.position[0]*64,
                    32+feu.position[1]*64,
                    image=self.photo_feu
                    )
        self.play()
        self.canvas.after(1000, self.update_canvas)
        
    def start(self):
        self.update_canvas()
        self.fen.mainloop()

    def play(self):
        for pompier in self.liste_pompiers:
            pompier.avancer_vers(self.feu_le_plus_proche(pompier))
        self.afficher()

    def afficher(self):
        for i in range(10):
            ligne = [self.quel_element(i,j) for j in range(10)]
            print(ligne)
    
    def quel_element(self, i, j):
        for pompier in self.liste_pompiers:
            if (pompier.position == np.array([i,j])).all():
                return 'P'
        for feu in self.liste_feux:
            if (feu.position == np.array([i,j])).all():
                return 'F'
        return ' '
    
    def eteindre(self, feu):
        self.liste_feux.remove(feu)
    
    def feu_le_plus_proche(self, pompier):
        feu_proche = self.liste_feux[0]
        for feu in self.liste_feux:
            if dist(feu, pompier) < dist(feu_proche, pompier):
                feu_proche = feu
        return feu_proche
    
