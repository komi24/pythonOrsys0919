# -*- coding: utf-8 -*-
from .Pompier import Pompier
from .Feu import Feu
import numpy as np


def dist(feu, pompier):
    return np.linalg.norm(feu.position - pompier.position)


class Terrain:
    def __init__(self):
        self.liste_pompiers = [Pompier(self) for i in range(3)]
        self.liste_feux = [Feu() for i in range(5)]
    
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
    
