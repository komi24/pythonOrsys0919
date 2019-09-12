# -*- coding: utf-8 -*-
import numpy as np
from random import randint as rd


class Pompier:
    def __init__(self, terrain):
        self.position = np.array([rd(0,9), rd(0,9)])
        self.est_disponible = 0
        self.terrain = terrain
        
    def avancer_vers(self, feu):
        if self.est_disponible == 0:
            if self.position[0] < feu.position[0]:
                self.position[0] += 1
            elif self.position[0] > feu.position[0]:
                self.position[0] -= 1
            elif self.position[1] < feu.position[1]:
                self.position[1] += 1
            elif self.position[1] > feu.position[1]:
                self.position[1] -= 1
            else:
                self.est_disponible = 5
        else:
            self.est_disponible -= 1
            if self.est_disponible == 0:
                self.terrain.eteindre(feu)
            
