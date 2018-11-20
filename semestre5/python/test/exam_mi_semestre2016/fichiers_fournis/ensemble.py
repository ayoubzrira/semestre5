"""
Fournit une classe "EnsemblePoints" permettant de stocker
un ensemble de points a relier dans l'ordre pour les jeux de dessin
pour enfants.
"""
from iterateurs import cases, couples, triplets

class EnsemblePoints:
    """
    ensemble de points a relier
    """
    def __init__(self, points):
        self.points = points

    def eliminer_doublons(self):
        """
        elimine les points consecutifs en double.
        exemple: [(0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (2.0, 2.0), (0.0, 0.0)]
        devient [(0.0, 0.0), (1.0, 0.0), (2.0, 2.0)].
        """
        nv_points = [p1 for p1, p2 in couples(self.points) if p1 != p2]
        self.points = nv_points

    def coordonnees_max(self):
        """
        renvoie les couples (x, y) de coordonnees maximales.
        par exemple, pour [(0.0, 0.0), (1.0, 3.0), (2.0, 2.0)]
        renvoie (2.0, 3.0).
        """
        return max(cases(self.points, 0)), max(cases(self.points, 1))


    def aire_triangle(self,triangle):
        """
        calcule l'aire d'un triangle
        """
        def produit(couple):
            "sous fonction qui calcule une partie de l'operation de calcul de l'aire"
            return couple[0][0] * couple[1][1] - couple[0][1] * couple[1][0]
        return abs(sum(produit(couples(triangle))))/2

    def simplification(self, nombre_points):
        """
        supprime des points jusqu'a ce qu'il ne reste plus que le
        nombre voulu.
        on considere pour chaque point le triplet qu'il forme
        avec son point precedant et son point suivant.
        chaque triplet forme un triangle d'une certaine aire.
        on elimine les points formant les plus petites aires.
        les points restants respectent l'ordre de depart.
        """
        points_interets = []
        for i, e in enumerate(triplets(self.points)):
            for i_e, point in enumerate(e):
                points_interets.append((i+i_e,self.aire_triangle(e)))
        print(points_interets)
        return points_interets
    def svg_vide(self, nom_fichier):
        """
        dessine les points a relier en svg (numerotes) dans le fichier donne.
        """
        self.svg_traits(nom_fichier, 0)

    def svg_traits(self, nom_fichier, nombre):
        """
        dessine les points a relier en svg (numerotes) dans le fichier donne.
        dessine egalement "nombre" traits, en partant du point 0.
        """
        entete_svg = '<svg width="{}" height="{}">'.\
        format(self.coordonnees_max()[0] + 10, self.coordonnees_max()[1] + 10)+"\n"
        arriere_plan_svg = '<rect width="{}" height="{}" fill = "white"/>'.\
        format(self.coordonnees_max()[0] + 10, self.coordonnees_max()[1] + 10) + "\n"
        pied_svg = '</svg>'
        with open(nom_fichier, "w") as fichier_svg:
            fichier_svg.write(entete_svg)
            fichier_svg.write(arriere_plan_svg)
            for i, point in enumerate(self.points):
                fichier_svg.write('<circle cx="{}" cy="{}" r="8" fill="red"/>\n'.\
                format(point[0], point[1]))
                fichier_svg.write('<text x="{}" y="{}">{}</text>\n'.format(point[0], point[1], i))
            for nb_traits, couple in enumerate(couples(self.points)):
                if nb_traits < nombre:
                    fichier_svg.write('<line x1="{}" y1="{}" x2="{}" y2="{}" \
                    stroke="red" stroke-width="8"/>'.\
                    format(couple[0][0], couple[0][1], couple[1][0], couple[1][1]))
                else:
                    break
            fichier_svg.write(pied_svg)


def lecture_ensemble(nom_fichier):
    """
    lit l'ensemble de points a partir d'un fichier (deux coordonnees par ligne)
    """
    with open(nom_fichier) as fichier:
        return EnsemblePoints([
            tuple([float(x) for x in ligne.split()])
            for ligne in fichier
        ])


def ensemble_test():
    """
    renvoie un ensemble contenant les trois points d'un petit triangle de test.
    """
    return EnsemblePoints([(10.0, 10.0), (300.0, 200.0), (150.0, 400.0)])
