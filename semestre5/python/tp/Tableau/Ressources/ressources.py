#!/usr/bin/env python3
"""
manipulations complexes de tableaux : listes d'intervalles.
"""


class Ressources:
    """
    On stocke une liste de ressources, compressee par plages contigues.
    """
    def __init__(self, nombre_ressources, intervalles=None):
        # requiert : si intervalles is not None, alors :
        #            - les intervalles sont non vides
        #            - les intervalles sont non contigus
        #            - les intervalles sont tries par indices croissants
        #            - intervalles[-1][1] <= nombre_ressources
        self.nombre_ressources = nombre_ressources
        if intervalles is not None:
            self.intervalles = intervalles
        else:
            self.intervalles = [[0, nombre_ressources]]

    def disponible(self, indice):
        """
        renvoie si l'indice donne est disponible dans la ressource.
        """
        for intervalle in self.intervalles:
            if indice in range(intervalle[0],intervalle[-1]) :
                return True
        return False



    def compression(self,tableau):
        tmp,res=[],[]

        prec = tableau[0]
        borne_sup = 0
        for i in tableau:
            if i == prec:
                tmp.append(i)
            elif (i-prec) == 1:
                borne_sup= i
            else:
                tmp.append(borne_sup+1)
                res.append(tmp)
                tmp = [i]
            prec = i
        #gestion du dernier el
        if len(tmp) == 1 and tableau[-1] == tmp[0]:
            tmp.append(tmp[0]+1)

        else:
            tmp.append(borne_sup+1)

        res.append(tmp)

        return res



    def difference_entre_tab(self,tab2):
            #tabs of tab
            res = []
            for value in self.decompression(self.intervalles):
                if value not in self.decompression(tab2):

                        res.append(value)
            return res

    def decompression(self,tab):
            res = []
            for inte in tab:
                for i in range(inte[0],inte[-1]):
                    res.append(i)
            return res

    def reserve(self, ressources_demandees):
        """
        enleve le nombre de ressources demandees (premieres disponibles).
        renvoie les ressources correspondant aux plages reservees.
        """
        if ressources_demandees < self.nombre_ressources:
            nb_ressourses_prises  = 0
            ressources_prises = []
            for i in range(self.nombre_ressources):
                if nb_ressourses_prises < ressources_demandees:
                    if self.disponible(i) and i != self.nombre_ressources:
                        ressources_prises.append(i)
                        nb_ressourses_prises += 1
                else:
                    break
        else:
            print("désolé ! il n y'a pas assez de ressources pour l'instant .")
            raise()
        ressources_prises = self.compression(ressources_prises)
          # les intervalles apres la reservation ( la diff entre intervalles actuels et ceux pris )
        if ressources_prises != self.intervalles:
            dif = self.compression(self.difference_entre_tab(ressources_prises))# li kayn f self.intervalles o matreservach
            self.intervalles = dif
        else:
            self.intervalles = [[self.nombre_ressources,self.nombre_ressources
        return Ressources(self.nombre_ressources,ressources_prises)



    def retourne(self, ressources_rendues):
        """
        remet les plages de ressources donnees dans le systeme.
        """
        # on a un objet ress qui contient tout ce qui a été pris
        # -> intervalles des ressources_prises
        # todo : ajouter ressources rendues aux intervalles de notre Ressources
        #print(" a " , self.intervalles)
         #print(" b " , ressources_rendues.intervalles[0])
        #print("hi " ,self.intervalles.insert(0,ressources_rendues.intervalles[0]))
        for i,intervalle in enumerate(ressources_rendues.intervalles):
            self.intervalles.insert(i,intervalle)
        #self.intervalles.append(ressources_rendues.intervalles)


    def __str__(self):
        """
        renvoie une chaine 'visuelle' des ressources contenues dans self.
        par exemple, '|x..xxxxx..|' indique qu'il y a 10 ressources,
        les ressources 0, 3-7 sont disponibles.
        """
        res = "|"
        for i in range(self.nombre_ressources):
            if self.disponible(i):
                res+= str(i) + "x"
            else:
                res += str(i) + "."

        res += "|"
        return res



def test():
    """
    on teste en gruyerisant une ressource.
    """
    #print(compression([0,1,2,4,5,6,9,10,11,13,14,19,20,21,22,205,206]))
    ressources = Ressources(10)
    #print("com " , ressources.compression([0,1,2,4,5,6,9,10,11,13,14,19,20,21,22,206]))

    print("Disponibles :", ressources)
    reservees = [ressources.reserve(c) for c in (2, 2, 3, 2, 1)]
    print("Disponibles :", ressources)
    ressources.retourne(reservees[1])
    print("Disponibles :", ressources)
    ressources.retourne(reservees[3])
    print("Disponibles :", ressources)
    print("Reservees   :", ressources.reserve(3))
    print("Disponibles :", ressources)
    print("Les intervalles :", ressources.intervalles)

if __name__ == "__main__":
    test()
