#!/usr/bin/env python3
"""
fichier principal pour l'utilisation des ensembles de points.
"""
from os import system
from ensemble import lecture_ensemble, ensemble_test

def main():
    """
    execute toutes les fonctions a programmer.
    """
    # affichage simple
    test = ensemble_test()
    print(test.coordonnees_max())
    test.svg_vide("test.svg")
    system("tycat test.svg")

    # a decommenter au fur et a mesure

   # lecture de fichier et affichage segments
    carre = lecture_ensemble("carre.txt")
    for traits in range(5):
        fichier = "t{}.svg".format(traits)
        carre.svg_traits(fichier, traits)
        system("tycat {}".format(fichier))
#
   # elimination redondance
    # carre_redondant = lecture_ensemble("carre_redondant.txt")
    # carre_redondant.svg_vide("red1.svg")
    # system("tycat red1.svg")
    # carre_redondant.eliminer_doublons()
    # carre_redondant.svg_vide("red2.svg")
    # system("tycat red2.svg")
#
#    # simplification
    etoile = lecture_ensemble("etoile.txt")
    etoile.svg_traits("etoile.svg", len(etoile.points))
    system("tycat etoile.svg")
    etoile.simplification(9)
    etoile.svg_traits("etoile2.svg", len(etoile.points))
#    system("tycat etoile2.svg")
#    etoile.simplification(3)
#    etoile.svg_traits("etoile3.svg", len(etoile.points))
#    system("tycat etoile3.svg")


main()
