#!/usr/bin/env python3

"""
     ce module divise un tableau en se basant sur un pivot
     on utilise dans un premier temps peu optimisée , en créant deux tableaux
     ensuite nous utiliserons une methode sans uiliser de tableaux additionnels
     mais en procédent par échanges des elements du tableau de depart
"""

def pivot_version1(tableau,indice_pivot):
    pivot = tableau[indice_pivot]
    tab1 , tab2 = [] , []
    for indice_element,element in enumerate(tableau):
        if indice_element != indice_pivot:
            if element <= pivot:
                tab1.append(element)
            elif element > pivot:
                tab2.append(element)
    return tab1 , tab2

# ____________________________________________________________


def pivot_version2(tableau,indice_pivot):
    pivot = tableau[indice_pivot]
    i_pivot = indice_pivot
    i = 0
    #for i,e in enumerate(tableau):
    while i <= len(tableau) - 1 :
        e = tableau[i]
        if i < i_pivot: # parti ' avant_pivot'
            if e > pivot:
                #proceder à un echange
                element_a_decaler = tableau.pop(i)
                tableau.insert(i_pivot,element_a_decaler)
                i_pivot -= 1
                i -= 1#pour ne pas souter des elements
            #sinon it's fine
        else: #parti " apres_pivot"
            if e <= pivot:
                element_a_decaler = tableau.pop(i)
                tableau.insert(i_pivot,element_a_decaler)
                i_pivot += 1
        i += 1
    tableau.pop(i_pivot)
    return tableau

def pivot_version3(tableau,indice_pivot):
    pivot = tableau[indice_pivot]
    tableau[-1],tableau[indice_pivot]=tableau[indice_pivot],tableau[-1]
    j = 0
    for i,e in enumerate(tableau):
        print(i , j)
        print(tableau)
        if e <= pivot:#tableau[i] < pivot
            tableau[i],tableau[j] = tableau[j],tableau[i]
            j += 1
    return tableau


#test version une :
#print(pivot_version3([1,0,10,1,6,9,5,3,9,0,5,8,9,8,4,2,0,9,6,2,0,0,0,2,2,6,9,5,2,1,5,9,5,2,2,0],7))

#test version deux
print(pivot_version3([1,3,2,0],2))
