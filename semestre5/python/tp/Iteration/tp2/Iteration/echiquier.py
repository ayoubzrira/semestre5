#!/usr/bin/env python3

class Rectangle:
    """
    modélise un rectangle
    un rectangle aura , un point de depart(x,y) , une largeur , hauteur et couleur ( blanc ou noir)
    """
    def __init__(self,x,y,hauteur,largeur,color):
        self.x = x
        self.y = y
        self.hauteur = hauteur
        self.largeur = largeur
        if not color :
            self.color = (0,0,0)
        elif color :
            self.color = (255,255,255)

    def __str__(self):
        affichage_rectangle = "<rect x='{}' y='{}' width='{}' height='{}' style='fill:rgb{}' />".format\
        (self.x,self.y,self.hauteur,self.largeur,self.color)
        return affichage_rectangle

class Echiquier:
    """
    notre echiquier sera un ensemble de rectangle blanc ou noir
    un echequier a un nb de colonne , nb ligne , une largeur, une hauteur . si on souhaite
    avoir un echequier de 0 ligne ou 0 colonne on aura un dessin vide
    """
    def __init__(self,hauteur,largeur,ligne,colonne):
        self.colonne = colonne
        self.ligne = ligne
        self.hauteur = hauteur
        self.largeur = largeur
        self.hauteur_rectangle = int(self.cote_xy()[0])
        self.largeur_rectangle = int(self.cote_xy()[0])

    def cote_xy(self):
        """
        retourne le nb de rectangles dans chaque ligne et chaque colonne
        """
        try:
            return (self.hauteur/self.ligne,self.largeur/self.colonne)
        except ZeroDivisionError:
            #print("ops , pas d echiquier de 0 lignes ou 0 colonnes")
            return 0,0

    """
    syntaxe svg ajout d un entete et pied
    """
    def entete(self):
        return "<svg width='{}' height='{}'>".format(self.largeur ,self.hauteur )

    def pied(self):
        return "</svg>"

    # def formation_echiquier(self):
    # """
    # renvoie une liste contenante tout les rectangles de l echequier
    # """
    #     res = []
    #     x,y = 0,0ZeroDivisionError: int
    #     for x in range(self.ligne):
    #         for y in range(self.colonne):
    #             if (x+y) % 2 == 0:
    #                 couleur = 1
    #             else:
    #                 couleur = 0
    #             c = Rectangle(x*self.hauteur_rectangle,y*self.largeur_rectangle,\
    #             self.hauteur_rectangle,self.largeur_rectangle,couleur)
    #             res.append(c)
    #     return res

    """
    affichage de l'Echiquier pour la syntaxe svg
    """
    def __iter__(self):

        for x in range(self.ligne):
            for y in range(self.colonne):
                if (x+y) % 2 == 0:
                    couleur = 1
                else:
                    couleur = 0
                yield Rectangle(x*self.hauteur_rectangle,y*self.largeur_rectangle,\
                self.hauteur_rectangle,self.largeur_rectangle,couleur)




    def __str__(self):

        affichage_echequier = self.entete()
        for rectangle in self:#.formation_echiquier():
            affichage_echequier += str(rectangle)
        affichage_echequier += self.pied()
        return affichage_echequier

def main():

    ech = Echiquier(1000,1000,0,1)
    #for e in ech:
    #     print(e)
    print(ech)


main()
