#!/usr/bin/env python3
# coding: utf-8

#%% Exercice 2


def somme(tab):
    s = 0
    for i in range(len(tab)):
        "à compléter"
        
    return s


# Tests unitaires   à décommenter    
#from random import randint
#for size in range(1, 5):
#    for run in range(10):
#        tab = [randint(-100, 100) for _ in range(size)]
#        assert(somme(tab)) == sum(tab), "Echec sur {}".format(tab)
#print("Tests unitaires réussis")


#%%Exercice 3


def moyenne(tableau):
    #décommenter et compléter
    #total = 
    for valeur in tableau:
        total = total + valeur
    return total / len(tableau)

# Tests unitaires   à décommenter  en sélectionnant le bloc puis CTRL + 1   
#from random import randint
#for size in range(1, 5):
#    for run in range(10):
#        tab = [randint(-100, 100) for _ in range(size)]
#        assert(moyenne(tab)) == sum(tab)/len(tab), "Echec sur {}".format(tab)
#print("Tests unitaires réussis")


#%% Exercice 4


def smul(k, tab):
    """
    Paramètres :
        k un nombre de type int ou float
        tab est un tableau de type list contenant des  nombres de type int ou float
    Précondition :
        tab non vide
    Valeur renvoyée :
        un tableau de type list contenant des  nombres de type int ou float
    Postcondition :
        le tableau renvoyé est constitué des produits 
        de chaque élément de tab par k
    """
    assert len(tab) != 0, "tab doit être non vide"
    # à décommenter et compléter
    # return 


def vsom(tab1, tab2):
    """
    Paramètres :
        tab1 et tab2 des tableaux de nombres de type int ou float
    Préconditions :
        tab1 non vide et len(tab1) == len(tab2)
    Valeur renvoyée :
        un tableau de type list contenant des  nombres de type int ou float
    Postcondition :
        le tableau renvoyé est constitué des sommes
        terme à terme des éléments de tab1 et tab2        
    """
    assert len(tab1) > 0 and len(tab1) == len(tab2); "tab1 et tab2 doivent être de même longueur"
    # à décommenter et compléter
    # return 


def vdiff(tab1, tab2):
    """A compléter !!!
    Paramètres :
        à compléter
    Précondition :
        à compléter
    Valeur renvoyée :
        à compléter
    Postcondition :
        le tableau renvoyé est constitué des différences terme à terme
        des éléments de tab2 et tab1 (la deuxième moins la première)        
    """
    #à compléter

def vprod(tab1, tab2):
    """A compléter !!!
    Paramètres :
        tab1 et tab2 sont des tableaux de type list contenant des  nombres de type int ou float
    Précondition :
        à compléter
    Valeur renvoyée :
        un tableau de type list contenant des  nombres de type int ou float
    Postcondition :
        le tableau renvoyé est constitué des produits
        terme à terme des éléments de tab2 et tab1 
    """
    #à compléter


#%% Exercice 5 Q1


def produit(tab):
    """
    Paramètres :
        tab est un tableau de type list contenant des  nombres de type int ou float
    Précondition :
        tab non vide
    Valeur renvoyée :
        un tableau de type list contenant des  nombres de type int ou float
    Postcondition :
        le tableau renvoyé est constitué du produit
        de tous les termes de tab
    """
    #à compléter

# Tests unitaires   à décommenter    en sélectionnant le bloc puis CTRL + 1  
#from random import randint
#from functools import reduce
#for size in range(1, 5):
#    for run in range(10):
#        tab = [randint(-100, 100) for _ in range(size)]
#        assert(produit(tab)) == reduce(lambda a, b: a * b,tab), "Echec sur {}".format(tab)
#print("Tests unitaires réussis")

#%% Exercice 5 Q2

def all_positive(tab):
    """
    Paramètres :
        tab est un tableau de type list contenant des  nombres de type int ou float
    Précondition :
        tab non vide
    Valeur renvoyée :
        un booléen
    Postcondition :
        la valeur renvoyée est 
            True si tous les éléments de tab sont positifs
            False sinon
    """
    assert len(tab) > 0, "le paramètre  doit être non vide"
    #à compléter


# Tests unitaires   à décommenter  en sélectionnant le bloc puis CTRL + 1    
#from random import randint
#from functools import reduce
#for size in range(1, 5):
#    for run in range(10):
#        tab = [randint(-100, 100) for _ in range(size)]
#        assert(all_positive(tab)) == all([e >= 0 for e in tab]), "Echec sur {}".format(tab)
#print("Tests unitaires réussis")


#%% Exercice 5 Q3

def any_positive(tab):
    """A compléter !!!
    Paramètres :
        tab est un tableau de type list contenant des  nombres de type int ou float
    Précondition :
        tab non vide
    Valeur renvoyée :
        un booléen
    Postcondition :
        la valeur renvoyée est 
            à compléter
    """
    assert len(tab) > 0, "le paramètre  doit être non vide"
    #à compléter

# Tests unitaires   à décommenter  en sélectionnant le bloc puis CTRL + 1    
#from random import randint
#from functools import reduce
#for size in range(1, 5):
#    for run in range(10):
#        tab = [randint(-100, 100) for _ in range(size)]
#        assert(any_positive(tab)) == any([e >= 0 for e in tab]), "Echec sur {}".format(tab)
#print("Tests unitaires réussis")


#%% Exercice 6

from random import randint

def tableau_aleatoire(n, a, b):
    """ 
    Paramètres :
       n, a et b trois entiers de type int
    Préconditions :
       n >= 0
       a <= b
    Valeur renvoyée :
       un tableau d'entiers de type list
    Postcondition :
        le tableau renvoyé contient  de n entiers tirés aléatoirement entre les entiers a et b inclus
    """
    assert a <= b and n >= 0
    #à compléter
  

def histo_echantillon(nbexp):
    """ 
    Paramètres :
       nbexp un entier de type int
    Préconditions :
       nbexp >= 0
    Valeur renvoyée :
       un tableau d'entiers de taille 6 de type list
    Postcondition :
        le tableau renvoyé contient le nombre d'occurences de chaque face de 1 à 6
        sur un échantillon de nbexp lancers de dé à 6 faces
    """
    assert nbexp >= 0, "la taille de l'échantillon doit être >= 0"
    histo = [0] * 6
    #à compléter

def tirage_sans_remise(urne):
    """ 
    Paramètres :
        urne un tableau homogène type list
    Précondition :
        urne non vide
    Valeur renvoyée :
        un élément du même type que ceux dans urne
    Postcondition :
        l'élement renvoyée a été extrait aléatoirement de urne
        urne a été modifiée
    """
    #à décommenter et à compléter
    #return urne.pop(randint(0, ))

def echantillon_tirage_sans_remise(urne : list, nbtirage : int) -> list:
    """ 
    Paramètres :
       urne un tableau homogène type list
       nbtirage un entier de type int
    Préconditions :
       nbtirage >= 0
       urne non vide
    Valeur renvoyée :
       un tableau d'entiers de type list
    Postcondition :
       le tableau renvoyé est un échantillon extrait
       aléatoirement de l'urne sans remise
    """
    assert len(urne) > 0 and nbtirage >= 0
    #à décommenter et à compléter
    #return 



#%% Exercice 7


#à décommenter et à compléter
#alphabet = 
#consonne = 

def occurences(chaine):
    """ 
    Paramètres :
       chaine de type str
    Préconditions :
       chaine non vide ? pas forcément
    Valeur renvoyée :
       un tableau de 26 entiers de type list
    Postcondition :
       le tableau renvoyé contient le nombre d'occurences 
       dans chaine des 26 lettres de l'alphabet romain.
    """
    histo = [0] * 26
    #à compléter
    return histo

# Tests unitaires   à décommenter en sélectionnant le bloc puis CTRL + 1     
#assert occurences('search') == [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
#assert occurences('occurences') == [0, 0, 3, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
#assert occurences('') == [0] * 26
#print('Tests unitaires réussis')


# %% Exercice 8


def fibonacci(n):
    """ 
    Paramètres :
       n un entier de type int
    Préconditions :
       n >= 0
    Valeur renvoyée :
       un tableau d'entiers de type list
    Postcondition :
       le tableau contient tous les termes de la suite de Fibonacci
       d'indices compris entre 0 et n
    """
    assert n>= 0
    #à compléter

# Tests unitaires   à décommenter  en sélectionnant le bloc puis CTRL + 1    
#f6 = fibonacci(6)
#assert f6 == [0,1, 1, 2,3,5]
#f30 = fibonacci(30)
#assert f30[29] == 514229
#print("Tests unitaires réussis !")



#%% Exercice 9

def arnaque(inputfile):
    """Résolution du problème 
    https://prologin.org/train/2019/qualification/arnaque_aerienne"""
    f = open(inputfile)  #ouverture du  fichier d'entrée
    # TO DO à compléter
    f.close() 
    c = 0
    # TO DO à compléter
    if c >= 3:
        print("ARNAQUE !")
        return 1
    else:
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")
        return 0

# Tests unitaires   à décommenter  en sélectionnant le bloc puis CTRL + 1     
#assert arnaque('arnaque-exemple1.txt') == 1
#assert arnaque('arnaque-exemple2.txt') == 0
#print("Tests unitaires réussis !")

#%% Exercice 10


def maximum_intervalle(t, n):
    """ 
    Paramètres :
       t un tableau de type list contenant des entiers de  type  int
       n un entier de type int
    Préconditions :
       len(t) >= 0
       0 <= n <= len(t)
    Valeur renvoyée :
       un entier de type int
    Postcondition :
       l'entier renvoyé est la somme maximale sur tous les sous-tableaux de 
       de longueur n
    """
    assert len(t) >= 0 and 0 <= n <= len(t)
    #à compléter

    
    
# Tests unitaires à décommenter en sélectionnant le bloc puis CTRL + 1  
#assert maximum_intervalle([4,1,10,2,8,5], 3) == 20
#assert maximum_intervalle([10,2,8,4,1,5], 3) == 20
#assert maximum_intervalle([4,1,5, 10,2,8], 3) == 20
#print("Tests unitaires réussis")

