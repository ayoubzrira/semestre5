#! /usr/bin/env python3

import sys


# formatage_fichier()

class Case:
    """
    Une case a une position et un état ( allumée ou eteinte)
    """
    def __init__(self,pos,etat):
        self.pos = pos
        self.etat = etat

    def __str__(self):
        return self.etat #. ou _

class Plateau:

    """
    Reconstruction du plateau à partir d'un fichier de niveau
    """
    def __init__(self):
        self.plateau =  self.creation_plateau()
        self.longueur = len(self.formatage_fichier())
        self.largeur = len(self.formatage_fichier())


    def deplacement_possible(self,depart):
        xd,yd = depart
        deplacements_possible = []
        for x in (-1,1):
            if xd+x in range(self.largeur):
                deplacements_possible += [(xd+x,yd)]
        for y in (-1,1):
            if yd+y in range(self.largeur):
                deplacements_possible += [(xd,yd+y)]

        return deplacements_possible




    def creation_plateau(self):
        for ligne,elem in enumerate(self.formatage_fichier()):
            for colonne,val in enumerate(elem):
                    yield Case((ligne,colonne),val)


    def formatage_fichier(self):
        fichier = sys.argv[1]
        niveau = open(fichier, "r")
        res = []
        for ligne in niveau:
            for elem in ligne[:-1]:
                res += [elem]
        return res

    def __str__(self):

        affichage = " " * 5
        borne_haut_bas = " "*3 + "+" + "_"*self.longueur*3 + "+" + "\n"
        for i in range(1,self.longueur+1):
            affichage += str(i) + " "*2
        affichage += "\n" + borne_haut_bas

        #    affichage += " " + chr(65+i) + " |"



        affichage += borne_haut_bas
        return affichage


def main():
    p = Plateau()
    print(p)
    print(p.deplacement_possible((0,2)))
main()
