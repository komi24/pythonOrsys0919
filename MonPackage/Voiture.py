# -*- coding: utf-8 -*-
import numpy as np


class Voiture:
    def __init__(
            self,
            position_initiale,
            couleur='pourpre',
            vitesse_max=130,
            nombre_de_place=2):
        self.couleur = couleur
        self.vitesse_max = vitesse_max
        self.nombre_de_places = nombre_de_place
        self.position = position_initiale
        self.direction = [0, 1]
    
    def avancer(self):
        """
        Fait la voiture avancer d'une fois la direction
        Sauf si la position sort du cadre [0,10]
        Dans ce cas elle tourne dans le sens horraire
        """
        new_position = np.array(self.position) + np.array(self.direction)
        if new_position[0] >= 0 and new_position[0] < 10 and \
            new_position[1] >= 0 and new_position[1] < 10:
            self.position = new_position
        else:
            self.tourner()
            self.avancer()
        
    def tourner(self):
        self.direction = np.array([[0,-1],[1,0]]).dot(self.direction)