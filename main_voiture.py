# -*- coding: utf-8 -*-

#from MonPackage.Voiture import Voiture

#une_voiture = Voiture([3,3])
#print(une_voiture.direction)
#une_voiture.tourner()
#print(une_voiture.direction)
#une_voiture.tourner()
#print(une_voiture.direction)
#une_voiture.tourner()
#print(une_voiture.direction)
#une_voiture.tourner()
#print(une_voiture.direction)

from MonPackage.Terrain import Terrain
from time import sleep
import os

mon_terrain = Terrain()

for i in range(10):
    os.system('clear')
    mon_terrain.play()
    sleep(1)