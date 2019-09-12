# -*- coding: utf-8 -*-
from Pompier.Terrain import Terrain
from time import sleep


terrain = Terrain()

for i in range(30):
    terrain.play()
    sleep(0.8)