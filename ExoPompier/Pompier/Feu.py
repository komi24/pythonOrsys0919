# -*- coding: utf-8 -*-
import numpy as np
from random import randint as rd


class Feu:
    def __init__(self):
        self.position = np.array([rd(0,9), rd(0,9)])