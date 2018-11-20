#!/usr/bin/env python3
"""
lecture d'un fichier de notes au format csv (3 examens)
et analyses
"""
from os import system

from debug import notes_statiques
from stats import parcours_notes, calcul_moyennes, etudiants_brillants, \
                  min_et_max, classement, histogramme


def ligne_separation():
    """
    affiche une petite ligne d'etoiles pour separer les differentes sorties
    """
    print("*" * 80)

def test_lecture_et_moyenne():
    """
    lit un fichier csv et affiche la moyenne a chaque examen.
    """
    notes = parcours_notes("notes.csv")
    if notes is None:
        print("a faire : completer la fonction 'parcours_notes'")
        notes = notes_statiques()

    moyennes = calcul_moyennes(notes)
    if moyennes is None:
        print("a faire : completer la fonction 'calcul_moyennes'")
    else:
        for numero, moyenne in enumerate(moyennes):
            print("pour l'epreuve numero {} la moyenne est {}".
                  format(numero, moyenne))

def test_brillants(etudiants):
    """
    affiche les etudiants avec un 20.
    """
    brillants = etudiants_brillants(etudiants)
    if brillants is None:
        print("a faire : completer la fonction 'etudiants_brillants'")
    else:
        print("les etudiants ayant au moins un 20 sont :",
              list(e.nom for e in brillants))

def test_min_et_max(etudiants):
    """
    affiche pour chaque examen les moins bons et les meilleurs.
    """
    m_and_ms = min_et_max(etudiants)
    if m_and_ms is None:
        print("a faire : completer la fonction 'min_et_max'")
    else:
        for numero, extremes in enumerate(m_and_ms):
            print("pour l'epreuve numero", numero)
            print("les moins bons sont :", list(e.nom for e in extremes[0]))
            print("les meilleurs sont :", list(e.nom for e in extremes[1]))

def test_classement(etudiants):
    """
    affiche le classement de la promo.
    """
    classe = classement(etudiants)
    if classe is None:
        print("a faire : completer la fonction 'classement'")
    else:
        print("le classement est :", "\n".join(str(e) for e in classe))

def test_histogramme(etudiants):
    """
    affiche les trois histogrammes des notes a chaque examens.
    """
    fichiers = [histogramme(etudiants, numero_epreuve) \
                   for numero_epreuve in range(3)]
    if fichiers[0] is None:
        print("a faire : completer la fonction 'histogramme'")
    else:
        for fichier in fichiers:
            system("tycat {}".format(fichier))

def main():
    """
    analyse d'un fichier de notes
    """

    ligne_separation()
    test_lecture_et_moyenne()

    etudiants = notes_statiques()
    #
    ligne_separation()
    test_brillants(etudiants)
    #
    ligne_separation()
    test_min_et_max(etudiants)
    #
    ligne_separation()
    test_classement(etudiants)
    #
    ligne_separation()
    test_histogramme(etudiants)

main()
