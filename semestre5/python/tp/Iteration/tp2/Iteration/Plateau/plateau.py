#!/usr/bin/env python3


class Case:

    """
    une case est definie par sa position (x,y) , son contenue(val) et
    son cote ( on le definie par default à 40 )
    """
    def __init__(self, x, y, val, c=40):
        self.x, self.y = x, y
        self.val = val
        self.c = c  # cote

    def __str__(self):
        affichage_rectangle = "<rect x=\"{}\" y=\"{}\" width=\"{}\" height=\"{}\" style=\"fill:rgb(255,255,255);stroke:black;stroke-width:1\"/>".format\
        (self.x,self.y,self.c,self.c) + "\n"
        affichage_text_dans_rectangle = "<text x=\"{}\" y=\"{}\"  font-size=\"20\" fill=\"red\"> {} </text>".format(self.x+self.c/20 , self.y+self.c/2 ,self.val) + "\n"

        return affichage_rectangle + affichage_text_dans_rectangle

class Pleateau:

    """
    """
    def __init__(self,h,l,cote_case):
        self.hauteur = h
        self.largeur = l
        self.nb_lignes = int(h/cote_case)
        self.nb_colonnes = int(l/cote_case)
        self.cote_case = cote_case

    """
    en tete et pied de page pour svg
    """

    def entete(self):
        return "<svg width=\"{}\" height=\"{}\">".format(self.largeur, self.hauteur)

    def pied(self):
        return "</svg>"
    """
    affichage des cases qui forment le plateau
    """
    def __iter__(self):
        fin,debut = 1,0 # vars qui definissent si le rectangle sera dessiné à gauche ou à droite dans le cas où il y'aura un seul rect dans la ligne
        compteur = 1 # sert à l afficheur des valeurs au milieu de la colonne
        for y in range(self.nb_lignes-1,-1,-1): #boucle à l envers
            for x in range(self.nb_colonnes):

                if y%2 == 0  :
                    if fin:
                        x =  self.largeur  - self.cote_case#on se position à la derniere colonne
                        fin,debut=0,1
                    else:#debut = 1
                        x = 0
                        fin,debut=1,0
                    yield Case(x,y*self.cote_case, compteur , self.cote_case)
                    compteur += 1
                    break # on break pour mettre une case sur cette ligne

                yield Case(x*self.cote_case,y *self.cote_case, compteur , self.cote_case)
                compteur += 1

    def __str__(self):
        plateau = self.entete() + "\n"
        for case in self:
            plateau += str(case) + "\n"
        plateau += self.pied()
        return plateau

def main():
    c = Case(10,10,1)
    p = Pleateau(1200,1200,40)
    print(p)
main()
