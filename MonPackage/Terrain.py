# -*- coding: utf-8 -*-
from .Voiture import Voiture
from random import randint

class Terrain:
    def __init__(self):
        self.liste_voitures = [Voiture(
                [randint(0,9),randint(0,9)]
                ) for i in range(10)]

    def play(self):
        for voiture in self.liste_voitures:
            voiture.avancer()
        self.afficher()
        
    def afficher(self):
        for i in range(10):
            ligne = ['x' if self._isVoiture(i,j) else ' ' for j in range(10)]
            print(''.join(ligne))

    def _isVoiture(self, i, j):
        """
            Renvoie true si une voiture occupe la position
            (i,j)
        """
        for voiture in self.liste_voitures:
            if voiture.position[0] == i and voiture.position[1] == j:
                return True
        return False
    def __repr__(self):
        return "Je suis un joli terrain avec " + str(self.liste_voitures)
    