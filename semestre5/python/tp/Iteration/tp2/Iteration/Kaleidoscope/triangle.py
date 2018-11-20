#!/usr/bin/env python3

from math import pi,cos,sin

from random import randint
from point import Point

class triangle_aleatoire:

    def __init__(self,minmax_largeur,minmax_hauteur):
        self.t = []
        for _ in range(3):
            self.t.append(Point([randint(minmax_hauteur[0],minmax_hauteur[1]),randint(minmax_largeur[0],minmax_largeur[1])]))

    def rotation_autour(self,centre,angle):
        angle_rad = angle * pi /180
        for p in self.t:
            p.x = (p.x - centre.x) * cos(angle_rad) - (p.y - centre.y) * sin(angle_rad) + centre.x
            p.y = (p.x - centre.x) * sin(angle_rad) + (p.y - centre.y) * cos(angle_rad) + centre.y
