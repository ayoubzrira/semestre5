#!/usr/bin/env python3

import sys
class Suite:
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

        suite_croissante = [e] #initialisation de la suite croissantes
        suite_decroissante = [e] #pareil

        while e != None:
            suivant = next(self.suite)#sauvegarder le prochain element
            #print("e : " , e , " suiv : " , suivant)
            if e < suivant:#strictement croissante
                yield suite_decroissante # on genere la derniere suite decroissante trouvée
                suite_decroissante = [suivant] #ensuite on la reinitialise avec l element suivant de la suite
                suite_croissante += [suivant]

            else:
                yield suite_croissante # on genere la derniere suite croissante trouvée
                suite_croissante= [suivant] #ensuite on la vide
                suite_decroissante += [suivant]#ensuite on la reinitialise avec l element suivant de la suite


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
