#!/usr/bin/env python3
from random import randint
class Point:

    def __init__(self,x,y):
        self.x = randint(0,200)
        self.y = randint(0,200)
    def __str__(self):
        affichagePoint = "<circle cx={} cy={}/>".format(self.x,self.y)
        return affichagePoint


class Triangle:
        def __init__(self,p1,p2,p3):
            self.t = [p1,p2,p3]

        def __str__(self):
            affichageTriangle = "<polygon points=\"{},{} {},{} {},{}\" />".format(self.t[0].x,self.t[0].y,\
            self.t[1].x,self.t[1].y,self.t[2].x,self.t[2].y)
            return affichageTriangle
class Dessin:
    def __init__(self,height,width):
        self.height = height
        self.width = width
    def entete(self):
        return  "<svg height=\"{}\" width=\"{}\">".format(self.height,self.width)
    def pied(self):
        return "</svg>"

def main():
    page = Dessin(200,500)

    p1 = Point(0,0)
    p2 = Point(0,100)
    p3 = Point(300,0)
    triangle = Triangle(p1,p2,p3)

    print(page.entete())
    print(triangle)
    print(page.pied())

main()
