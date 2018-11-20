#! /usr/bin/env python3


def cases(donnees, indice):
    """
    genere les elements d'un indice donné
    """
    for element in donnees:
        yield element[indice]

def couples(donnees):
    iterateurs = iter(donnees)
    debut = next(iterateurs)
    prec = debut
    for cour in iterateurs:
        yield prec,cour
        prec = cour
    yield prec,debut

def triplets(donnees):
    #donnees = iter(donnees)
    for i,e in enumerate(donnees):
        print(i)
        yield donnees[i-1],donnees[i],donnees[(i+1) % len(donnees) ]
