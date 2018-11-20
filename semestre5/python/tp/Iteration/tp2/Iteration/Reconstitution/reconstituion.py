#!/usr/bin/env python3
import sys
class Point:
    """
    crée un point qui est par default le centre (0,0)
    """
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def set_coords(self):
        self.x = int(input())
        self.y = int(input())

    def draw_svg(self):
        print("<svg height=\"640\" width=\"480\">")
        print("<cicle cx='{}' cy='{}' r='40' stroke='red' stroke-width='3' fill='red'/>".format(self.x,self.y))
        print("</svg>")

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

def iter_fichier():
    """
    genere un itérateur de l'entrée standart ( fichier )
    """
    for d in sys.stdin:
        yield d

def formater_fichier():
    """
    met les coords qui sont dans le fichier donné à l entrée standart
    dans une liste de tuple , dont chaque tuple contient les deux coords
    d un point , qui sont presenté dans le fichier dans une ligne l'un apres
    l'autre
    """
    fichier = iter_fichier()
    points = []
    for coord in fichier:
        points.append((int(coord),int(next(fichier))))#(x,y)
    return points

def main():
    p = Point()
    print(p)
    p.set_coords()
    p.draw_svg()


main()
