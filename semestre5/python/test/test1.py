#!/usr/bin/env python3
from Point import *


def entete(hauteur,largeur):
    print("<svg height={} width={}>".format(hauteur,largeur))

def triangle():
    triangle = [Point(),Point(),Point()]


    print("<polygon points=\"{}\" \"{}\" \"{}\" />".format(triangle[0].svg(),triangle[1].svg(),triangle[2].svg()))

def pied():
    print("</svg>")

def main():
    entete(200,500)
    triangle()
    pied()

main()
