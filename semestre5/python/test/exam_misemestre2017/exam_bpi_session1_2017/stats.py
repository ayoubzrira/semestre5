
"""
quelques fonctions pour l'analyse de notre fichier de notes
"""
# remplacer les valeurs de ces variables par les valeurs vous correspondant
# en majuscules pour NOM et PRENOM, un entier entre 1 et 8 pour GROUPE
NOM = "ZRIRA"
PRENOM = "Ayoub"
GROUPE = 8

print("vous etes '{}, {}', etudiant dans le groupe {}".format(NOM, PRENOM, GROUPE))

class Etudiant:
    """
    les infos pour un etudiant
    """
    #pylint: disable=too-few-public-methods
    def __init__(self, prenom, nom, notes):
        """
        note : les trois notes sont des entiers entre 0 et 20
        """
        self.prenom = prenom
        self.nom = nom
        self.notes = notes

def parcours_notes(nom_fichier):
    """
    ouvre le fichier de notes (dont le nom est nom_fichier)
    et itere sur tous les etudiants (de la classe Etudiant)
    """
    with open(nom_fichier, "r") as fichier_notes:
        # TODO: a completer :

        # parcourir les lignes et faire un yield de chaque objet Etudiant
        for ligne in fichier_notes:
            if ligne is not None:
                prenom, nom, note0, note1, note2 = ligne.split(',')
                yield Etudiant(prenom, nom, [note0, note1, note2])




def calcul_moyennes(etudiants):
    """
    prend un *iterable* sur les etudiants,
    renvoie un triplet contenant les moyennes de la promo a chaque examen.
    """
    s0, s1, s2 , nb_etu = 0,0,0,0
    for e in etudiants:
        nb_etu += 1
        s0 += int(e.notes[0])
        s1 += int(e.notes[1])
        s2 += int(e.notes[2])
    return (s0/nb_etu, s1/nb_etu, s2/nb_etu)


def etudiant_avec_note_max(note):
    #notes_f=[int[n] for n in notes]
#    notes = iter(notes)



    if note == 20:
            return True


    return False

def etudiants_brillants(etudiants):
    """
    prend un *iterable* sur les etudiants,
    itere sur les etudiants ayant au moins un 20.
    a implementer si possible a l'aide de la fonction "filter".
    """
    for e in etudiants:
        if 20 in filter(etudiant_avec_note_max,e.notes):
            yield e

def calcul_mini_maxi(etudiants):
    """

    """
    notes0 = [e.notes[0] for e in etudiants]
    notes1 = [e.notes[1] for e in etudiants]
    notes2 = [e.notes[2] for e in etudiants]
    return ((min(notes0),max(notes0)), (min(notes1),max(notes1)), (min(notes2),max(notes2)))

def min_et_max(etudiants):
    """
    prend un *iterable* sur les etudiants,
    renvoie un triplet de couples de vecteurs :
    pour chaque epreuve, tous les etudiants ayant
    la note minimale et tous les etudiants ayant la note maximale.
    """
    min_max = calcul_mini_maxi(etudiants)

    e_min0 = [e for e in etudiants if min_max[0][0] == e.notes[0]]
    e_max0 = [e for e in etudiants if min_max[0][1] == e.notes[0]]
    e_min1 = [e for e in etudiants if min_max[1][0] == e.notes[1]]
    e_max1 = [e for e in etudiants if min_max[1][1] == e.notes[1]]
    e_min2 = [e for e in etudiants if min_max[2][0] == e.notes[2]]
    e_max2 = [e for e in etudiants if min_max[2][1] == e.notes[2]]
    return (e_min0,e_max0), (e_min1,e_max1), (e_min2, e_max2)

def take_second(elem):
    return elem[1]
def classement(etudiants):
    """
    prend un *iterable* sur les etudiants,
    renvoie un vecteur de couples (nom, moyenne) de tous les etudiants,
    tries selon leur moyenne.
    la moyenne est obtenue avec les coefficients suivants :
    1 pour l'epreuve 0, 1 pour l'epreuve 1 et 2 pour l'epreuve 2
    """
    #on calcule d'abord la moyenne de chaque étudiant
    moyennes = []
    for e in etudiants:
        moyenne = ((e.notes[0] + e.notes[1]) + 2*e.notes[2])/4
        moyennes.append((e.nom,moyenne))
        print(moyenne)
    #classer les etudiants
    return sorted(moyennes,key=take_second)

def nb_etudiants_ayant_lanote(etudiants,numero_epreuve,n):
    cpt = 0
    for e in etudiants:
        if e.notes[numero_epreuve] == n:
            cpt +=1
    return cpt

def histogramme(etudiants, numero_epreuve):
    """
    prend un *iterable* sur les etudiants et le numero d'une epreuve.
    genere un histogramme en baton des notes, en svg a l'aide de rectangles,
    et renvoie le nom du fichier genere
    """
    svg = ""
    entete_svg ='<svg width="420" height="500">'
    svg += entete_svg + "\n"
    arriere_plan = '<rect width="420" height="500" fill="white"/>'
    svg += arriere_plan + "\n"
    for i in range(21):
        nb_etu = nb_etudiants_ayant_lanote(etudiants,numero_epreuve,i)
        svg += '<text x="{}" y="320">{}</text>\n'.format(i*20,i)
        if nb_etu != 0:
            svg += '<rect width="20" height="{}" x={} y="100" fill="red"/>\n'.format(20*nb_etu,i*20)
    svg += '<\svg>'
    return svg
