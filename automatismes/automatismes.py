# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
#%%Automatisme 1

def index_min(t):
    """
    Paramètre : t un tableau de nombres (int ou float)
    Précondition : t non vide
    Valeur renvoyée : un tableau contenant les positions (index) où le minimum de t est atteint
    """
    assert len(t) > 0
    tmin = t[0]
    tpos = [0]
    for i in range(1, len(t)):
        if t[i] < tmin:
            tmin = t[i]
            tpos = [i]
        elif t[i] == tmin:
            tpos.append(i)
    return tpos
    
    
#%%Automatisme 2
    
def au_moins_un_zero(t):
    """
    Paramètre : t un tableau de nombres (int ou float)
    Précondition : t non vide
    Valeur renvoyée : un booléen indiquant si t contient au moins un zéro
    """
    for e in t:
        if e  == 0:
            return True
    return False

##%Automatisme 3
    
#bin(49)
#Out[7]: '0b110001'

#%%Automatisme 6
    
def liste_chiffres(n):
    L = [n % 10]
    while n >= 10:
        n = n // 10
        L.insert(0, n % 10)
    return L


##%Automatisme 7
    
def image_noire(largeur, hauteur):
    """
    Paramètre : 
        largeur et hauteur deux entiers non nuls
    Valeur renvoyée :
        un tableau à 2 dimensions représentant une image
        binaire de dimensions (largeur, hauteur)
        rempli de 0
    """
    return [[0 for i in range(largeur)] for j in range(hauteur)]
    
def dimensions(tab):
    """
    Paramètre : 
        tab un tableau à deux dimensions d'entiers
        représentant une image binaire rectangulaire
    Valeur renvoyée :
        un tableau de deux entiers [largeur, hauteur]
        représentant les dimensions de l'image
    """
    return [len(tab[0]), len(tab)]
    
def nombre_blancs(tab):
    """
    Paramètre : 
        tab un tableau à deux dimensions d'entiers
        représentant une image binaire rectangulaire
    Valeur renvoyée :
        un entier représentant le nombre de pixels 
        blancs (valeur 1)
    """
    c = 0
    largeur, hauteur = dimensions(tab)
    for col in range(largeur):
        for lig  in range(hauteur):
            if tab[lig][col] == 1:
                c = c + 1
    return c

#postconditions pour la fonction image_noire 
assert image_noire(2,1) == [[0,0]]
assert image_noire(1,2) == [[0], [0]]
assert image_noire(3,2) == [[0,0,0], [0,0,0]]


#postconditions pour la fonction dimensions 
assert dimensions([[], []]) == [0,2]
assert dimensions([[0,1,2], [3,4,5]]) == [3,2]

#postconditions pour la fonction nombre_blancs
assert nombre_blancs([[0,0], [0,0]]) == 0
assert nombre_blancs([[0,1,1], [0,1,0]]) == 3
assert nombre_blancs([[], []]) == 0


#%%Automatismes  8 et 9

# Fonction de tri dans l'ordre croissant par sélection du maximum

def indice_maximum(tab, debut, fin):
    """
    Paramètres : 
        tab un tableau d'entiers
        debut un entier indice du début de la plage
        fin un entier indice de la fin de la plage (inclus)
    Valeur renvoyée : l'indice de la première occurence du maximum de tab 
    dans la plage  de valeurs entre les indice et debut et fin (inclus)
    """
    imax = debut
    for i in range(debut + 1, fin + 1):
        if tab[i] > tab[imax]:
            imax = i
    return imax
    
    
def tri_selection(tab):
    """
    Paramètre : tab un tableau de nombres
    Valeur renvoyée : tab
    Postcondition : valeur renvoyée de tab triée dans l'ordre croissant
    """
    i = len(tab) - 1
    while i >= 1:
        imax = indice_maximum(tab,0, i)
        tab[i], tab[imax] =  tab[imax], tab[i]
        # assertion qui doit être vérifiée
        assert max(tab[:i+1]) == tab[i]
        i = i- 1
    return tab 
    
# Tests unitaires

import random


def test_indice_maximum(fonction_indice_maximum):
    #tableaux aléatoires
    for size in range(1, 10):
        tab = [random.randint(0, 100) for _ in range(size)]
        assert fonction_indice_maximum(tab, 0, len(tab) - 1) == tab.index(max(tab))
    print(f"Tests unitaires réussis pour {fonction_indice_maximum.__name__}")
    
def test_tri(fonction_tri):
    """Test unitaire d'une fonction de tri"""
    #tableaux déjà triés
    for size in range(0, 10):
        tab = list(range(0, size))
        assert fonction_tri(tab) == sorted(tab), f"echec sur {tab}"
    #tableaus triés dans l'ordre inverse
    for size in range(0, 11):
        tab = list(range(9 - size, -1, -1))
        assert fonction_tri(tab) == sorted(tab), f"echec sur {tab}"
    #tableaux aléatoires
    for size in range(0, 10):
        tab = [random.randint(0, 100) for _ in range(size)]
        assert fonction_tri(tab) == sorted(tab), f"echec sur {tab}"
    print(f"Tests unitaires réussis pour {fonction_tri.__name__}")

#désactiver pour effectuer les tests unitaire      
test_indice_maximum(indice_maximum)
test_tri(tri_selection)


#%%Automatisme 11

def un_doublon(t):
    """
    Paramètre : t un tableau de nombres
    Valeur renvoyée : un booléen 
        True si t comporte au moins un doublon
        False sinon
    """
    for i in range(1, len(t) - 1):
        for j in range(i + 1, len(t)):
            if t[i] == t[j]:
                return True
    return False

assert un_doublon([1, 2, 3]) == False
assert un_doublon([1, 2, 2]) == True
assert un_doublon([1, 2, 4, 2]) == True
assert un_doublon([]) == False
print("Tests unitaires réussis pour la fonction un_doublon")

#%%Automatisme 10

import random

## Fonctions outils

def permute(tab, i, j):
    """
    Paramètres : 
        t un tableau de nombres  et element un nombre
    Postcondition : 
        permutation des éléments de t d'indices i et j
    """
    tab[i], tab[j] = tab[j], tab[i]
    
def inserer(element, tab):
    """
    Paramètres : 
        t un tableau de nombres trié dans l'ordre croissant
        element un nombre
    Postcondition : 
        insère element dans tab à sa place
    """
    tab.append(element)
    j = len(tab) - 1
    while j > 0 and tab[j - 1] > tab[j]:
        permute(tab, j - 1, j)
        j = j - 1

## k plus petits éléments 

def plus_petit(k, t):
    """"
    Paramètres : 
        k un entier
        t un tableau de nombres
    Précondition : 
        len(t) >= k  
    Valeur renvoyée : 
        un tableau de nombres contenant les k plus petits
        éléments de t
    """
    assert len(t) >= k
    kpetit = []
    if k == 0:
        return kpetit
    for i in range(len(t)):
        if  i < k or kpetit[k-1] > t[i]:
            inserer(t[i], kpetit)
            if len(kpetit) > k:
                kpetit.pop()
    return kpetit

def test_unitaire_plus_petit(fonction):
    for taille in range(0, 10):
        t = [random.randint(0, 100) for _ in range(taille)]
        for k in range(0, taille):
            assert plus_petit(k, t) == sorted(t)[:k]
    print(f"Tests unitaires réussis pour la fonction {fonction.__name__}")

# Décommenter pour effectuer les tests unitaires pour la fonction plus_petit

test_unitaire_plus_petit(plus_petit)

## Tri par dénombrement
    
def tri_denombrement(t, n):
    """
    Paramètre : t un tableau denombres et binf et bsup deux entiers
    Precondition : toutes les valeurs de t entre 0 et n
    Valeur renvoyée : un tableau où les éléments de t sont triés
    dans l'ordre croissant
    """
    histo = [0 for _ in range(n + 1)]
    for e in t:
        histo[e] = histo[e] + 1
    t_ordre = []
    for k in range(n + 1):
        t_ordre = t_ordre + [k for _ in range(histo[k])]
    return t_ordre
    
def tri_denombrement2(t, n):
    """
    Paramètre : t un tableau denombres et binf et bsup deux entiers
    Precondition : toutes les valeurs de t entre 0 et n
    Valeur renvoyée : un tableau où les éléments de t sont triés
    dans l'ordre croissant
    """
    if len(t) == 0:
        return []
    histo = [0 for _ in range(n + 1)]
    for e in t:
        histo[e] = histo[e] + 1
    t_ordre = [0 for _ in range(len(t))]
    k = 0
    i = 0
    while k <= n:
        if histo[k] > 0:
            histo[k] = histo[k] - 1
            t_ordre[i] = k
            i = i + 1
        else:
            k = k + 1
    return t_ordre
    
def test_unitaire_denombrement(fonction):
    for n in range(0, 10):
        for taille in range(0, 10):
            t = [random.randint(0, n) for _ in range(taille)]
            assert fonction(t, n) == sorted(t)
    print(f"Tests unitaires réussis pour la fonction {fonction.__name__}")
    
# Décommenter pour effectuer les tests unitaires pour la fonction tri_denombrement
test_unitaire_denombrement(tri_denombrement)
test_unitaire_denombrement(tri_denombrement2)

    

#%%Automatisme 12
def index_premiere_occurence_dicho(x, t):
    """
    Paramètre : 
        t un tableau de nombres trié dans l'ordre croissant
        x un nombre 
    Valeur renvoyée : 
        l'index de la première de x dans t si x est dans t
        -1 sinon
    """
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] < x:
            a = m + 1
        elif t[m] > x:
            b = m - 1
        else:
            p = m
            while p >= 1 and t[p-1] == x:
                p = p - 1
            return p
    return -1

assert index_premiere_occurence_dicho(10, [10, 10, 11, 12, 13]) == 0
assert index_premiere_occurence_dicho(10, [9, 10, 11, 12, 13]) == 1
assert index_premiere_occurence_dicho(10, [9, 9, 11, 12, 13]) == -1
assert index_premiere_occurence_dicho(10, [7, 8, 9, 10]) == 3 
assert index_premiere_occurence_dicho(10, [7, 10, 10,  10, 10]) == 1 
assert index_premiere_occurence_dicho(10, []) == -1
print("Tests unitaires réussis pour la fonction index_premiere_occurence_dicho")


#%% Automatisme 13

def est_decroissant(t):
    """
    Paramètre : 
        t un tableau de nombres 
    Valeur renvoyée : 
        booléen indiquant si t dans l'ordre décroissant
    """
    for i in range(0, len(t) - 1):
        if t[i] < t[i + 1]:
            return False
    return True


def recherche_dicho_decroissant(x, t):
    """
    Paramètre : 
        t un tableau de nombres trié dans l'ordre décroissant
        x un nombre 
    Valeur renvoyée : 
        index de x dans t si x dans t
        None si x pas dans t
    """
    a = 0
    b = len(t) - 1
    while a <= b:
        m = (a + b) // 2
        if t[m] > x:
            a = m + 1
        elif t[m] < x:
            b = m - 1
        else:
            return m
    return None

assert est_decroissant([k ** 2 for k in range(10)]) == False
assert est_decroissant([]) == True
t1 = list(range(10, -1, -1))
assert est_decroissant(t1) == True
assert recherche_dicho_decroissant(8, t1) == 2
assert recherche_dicho_decroissant(10, t1) == 0
assert recherche_dicho_decroissant(0, t1) == 10
assert recherche_dicho_decroissant(4.5, t1) == None
print("Test unitaires réussis pour l'automatisme 13 : recherche_dicho_decroissant et est_decroissant")


#%% Automatisme 17 

def recherche(elt, tab):
    """Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre entier et `tab`
un tableau de nombres entiers, et qui renvoie l’indice de la première occurrence de `elt`
dans tab si elt est dans tab et -1 sinon."""
    for k in range(len(tab)):
        if tab[k] == elt:
            return k
    return -1

assert recherche(10, [14,10,10]) == 1
assert recherche(11, [14,10,10]) == -1

#%% Automatisme 18 


def maxi(tab):
    """Écrire une fonction maxi qui prend en paramètre une liste tab de nombres entiers et
renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la
première apparition de ce maximum dans la liste."""
    assert len(tab) > 0
    ind_maxi = 0
    maxi = tab[0]
    for k in range(1, len(tab)):
        if tab[k] > maxi:
            maxi = tab[k]
            ind_maxi = k
    return (maxi, ind_maxi)

assert maxi([1,5,6,9,1,2,3,7,9,8]) == (9, 3)

#%% Automatisme 19

def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while i >= 0 and a < l[i]: 
      l[i+1] = l[i]
      l[i] = a
      i = i - 1
    return l

assert insere(3,[1,2,4,5]) == [1, 2, 3, 4, 5]
assert insere(10,[1,2,7,12,14,25]) == [1, 2, 7, 10, 12, 14, 25]
assert insere(1,[2,3,4]) == [1,2,3,4]



# %% Automatisme 20

def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0 
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
             fin = m - 1			
    return False

assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28) == True
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27) == False

#%% Automatisme 21

def tri_selection(tab):
    """Écrire une fonction `tri_selection` qui prend en paramètre 
    un tableau tab de nombres entiers
     et qui renvoie le tableau trié par ordre croissant.
    On utilisera l’algorithme suivant :

    * on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice
    0 ;
    * on recherche le second plus petit élément du tableau, et on l'échange avec l'élément
    d'indice 1 ;
    * on continue de cette façon jusqu'à ce que le tableau soit entièrement trié dans l'ordre croissant.
    """
    for i in range(0, len(tab)):
        imin = i
        for j in range(i + 1, len(tab)):
            if tab[j] < tab[imin]:
                imin = j
        tab[imin], tab[j] = tab[j], tab[imin]
    return tab

assert tri_selection([1,52,6,-9,12]) == [-9, 1, 6, 12, 52]
assert tri_selection([]) == []
assert tri_selection([1, 4, 8]) == [1, 4, 8]
assert tri_selection([8, 4, 1]) == [1, 4, 8] 

#%% Automatisme 22

def inverse_chaine(chaine):
    result = ""
    for caractere in chaine:
       result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

assert inverse_chaine('bac') == 'cab'
assert est_palindrome('NSI') == False
assert est_palindrome('ISN-NSI') == True
assert est_nbre_palindrome(214312) == False
assert est_nbre_palindrome(213312) == True
#%% Automatisme 23

Compléter la fonction `separe` ci-dessous qui prend en argument un tableau tab dont
les éléments sont des 0 et des 1 et qui sépare les 0 des 1 en plaçant les 0 en début de
tableau et les 1 à la suite.

def separe(tab):
    """prend en argument un tableau tab dont
    les éléments sont des 0 et des 1 et qui sépare les 0 des 1 
    en plaçant les 0 en début de tableau et les 1 à la suite.
    """
    i = 0
    j = len(tab) - 1
    while i < j :
        if tab[i] == 0 :
            i = i + 1
        else :
            tab[i], tab[j] = tab[j], tab[i]
            j = j - 1
    return tab


assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#%% Automatisme 24

def indice_du_min(tab):
    """prend en paramètre un tableau de nombres non
    trié tab, et qui renvoie l'indice de la première occurrence du minimum de ce tableau. Les
    tableaux seront représentés sous forme de liste Python."""
    assert len(tab) > 0
    ind_mini = 0
    mini = tab[0]
    for k in range(1, len(tab)):
        if tab[k] < mini:
            mini = tab[k]
            ind_mini = k
    return ind_mini

assert  indice_du_min([5])  == 0
assert indice_du_min([2, 4, 1]) == 2
assert indice_du_min([5, 3, 2, 2, 4]) == 2


# %%
