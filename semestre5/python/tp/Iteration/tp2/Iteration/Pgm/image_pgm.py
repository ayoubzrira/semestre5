#!/usr/bin/env python3

from random import randint
from math import sqrt

class Disque:
    """
    création d un disque , avec un centre x,y et un rayon r qui sont initialisé
    aléatoirement ( avec une hauteurMax et une largeurMax)
    """
    def __init__(self,hauteurMax,largeurMax):
        self.x = randint(0,largeurMax)
        self.y = randint(0,hauteurMax)
        self.r = randint(0,largeurMax)

    def distance_centre_point(self,xp,yp):
        """
        calcul la distance entre le centre du disque et un autre point
        ca sera utilisé pour savoir si un point appartient au cercle ou pas
        """
        return sqrt((xp-self.x)**2 + (yp-self.y)**2 )


class Pixel:
    """
    chaque point de la page Pgm sera un pixel
    """
    def __init__(self,x,y,val):

        self.x = x
        self.y = y
        self.val = val

class Pgm:
    def __init__(self,valeurMax=255,typeFichier="P2"):
        self.typeFichier = typeFichier
        self.hauteur = int(input())#"entrez la hauteur de l'image"
        self.largeur = int(input())#"entrez la largeur de l'image"
        self.valeurMax = valeurMax
        self.disque = Disque(self.hauteur,self.largeur)
        self.disque2 = Disque(self.hauteur,self.largeur)

    """
      syntaxe de base d'un fichier .pgm (3 premiéres lignes)
    """
    def entete(self):
        entete_pgm = self.typeFichier + " \n"
        entete_pgm += str(self.largeur) + " " + str(self.hauteur) + "\n"
        entete_pgm += str(self.valeurMax) + "\n"
        return entete_pgm

    """
    affichage selon la norme d'un fichier .pgm
    """
    def __iter__(self):
        # if self.hauteur <= 0 or self.largeur <= 0 : #gestion des cas speciaux
        #     yield Pixel(0,0,0)
            for ligne in range(self.hauteur):
                for colonne in range(self.largeur):
                    yield Pixel(ligne,colonne,0)

    def __str__(self):
        conversion_pgm = self.entete()
        pos = 0
        for pix in self:
            if (self.disque.distance_centre_point(pix.x,pix.y) <= self.disque.r) or (self.disque2.distance_centre_point(pix.x,pix.y) <= self.disque2.r):
                pix.val = randint(0,self.valeurMax)
            else:
                pix.val = 255
            conversion_pgm += str(pix.val) + " "
            pos +=1
            if pos%self.largeur == 0:
                conversion_pgm += "\n" #si on affiche le max d une ligne(largeur demandée) je reviens à la ligne

        return conversion_pgm

def main():
    test = Pgm()
    print(test)
main()
