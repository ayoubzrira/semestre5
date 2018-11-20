#!/usr/bin/env python3

import sys
class Suite:
    """
    prend un fichier contenant une suite de nombre et
    genere la plus grande sous_suite monotone
    """
    def __init__(self):
        self.fichier = sys.argv[1]
        self.suite = self.iterateur_nombre_fichier()


    def iterateur_nombre_fichier(self):
        """
        genere une suite de nombre à partir d'un fichier
        """
        mon_fichier = open(self.fichier, "r")
        for ligne in mon_fichier:
            for element in  ligne.replace("\n","").split(" "):
                yield element


    def iterateur_sous_suite(self):
        """
        genere des sous suites croissantes ou decroissante à partir
        d'une suite de nombre
        """
        e = next(self.suite) #premier element de la suite

        suite = [e]
        croissante = True
        while e != None:
            suivant = next(self.suite)#sauvegarder le prochain element

            if e < suivant:#strictement croissante
                if not croissante:
                    croissante = True
                    yield suite# on genere la derniere suite decroissante trouvée
                    suite = [e] #ensuite on la reinitialise avec l element suivant de la suite

            else:
                if croissante:
                    croissante = False
                    yield suite
                    suite = [e]
                
            suite += [suivant]
            e = suivant#on se decale un cran devant ( l element actuel est le suivant de la suite)

    def max(self):
        """
        retourne la plus longue sous suite generée
        """
        return max(self.iterateur_sous_suite(),key=len)


def main():
    s = Suite()
    print(s.max())

main()
