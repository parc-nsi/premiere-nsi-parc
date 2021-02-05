#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:11:48 2020

@author: frederic.junier
"""

#%% Passage de paramètres

def incremente(x):
    x = x + 1
    return x
    
def incremente_tab(tab):
    for k in range(len(tab)):
        tab[k] = tab[k] + 1
        
        
a = 5
t1 = [5, 6, 7]
t2 = t1
b = incremente(a)
incremente_tab(t1)

#%% Exercice 7 instruction assert


#assert a < b, "a doit être <  à b"
#
#
#
#a, b = b, a
#
#assert a < b, "a doit être <  à b"
#Traceback (most recent call last):
#
#  File "<ipython-input-11-3ab3dd6e1909>", line 1, in <module>
#    assert a < b, "a doit être <  à b"
#
#AssertionError: a doit être <  à b


#%% Exo 7 Q1

def echange(tab, i, j):
    assert 0 <= i < len(tab) and 0 <= j < len(tab), "erreur"
    tab[i], tab[j] = tab[j], tab[i]
    #on modifie tab par effet de bord
    #pas de return la fonction renvoie None
    
t1 = [k ** 2 for k in range(11)]
t2 = [k for k in range(21) if k % 3 == 0]
echange(t1, 0, 11)
print(t1)
assert t1 == [4, 1, 0, 9, 16, 25, 36, 49, 64, 81, 100]
    

#%% Méthodes de tableau dynamique 


#%% Exercice 8

def filtre_notes(tab):
    tinf = []
    for k in range(len(tab)):
        if tab[k] < 10:
            tinf.append(tab[k])
    return tinf


def filtre_notes2(tab):
    tinf = []
    for note in tab:
        if note < 10:
            tinf.append(note)
    return tinf

def filtre_notes3(tab):
    return [note for note in tab if note < 10]

notes = [5,7,8,14,10,9,14, 7]

def pos_maximum_tab(tab):
    """Renvoie l'élément maximum de tab
    et la liste des positions où il est atteint
    """
    assert len(tab) > 0, "tab doit etre non vide"
    pos = []
    maxi = tab[0]
    for k in range(len(tab)):
        if tab[k] > maxi:
            maxi = tab[k]
            pos = [k]
        elif tab[k] == maxi:
            pos.append(k)
        print(tab[k], maxi, pos)
    return [maxi, pos]


def maximum_tab(tab):
    """Renvoie l'élément maximum de tab"""
    assert len(tab) > 0, "tab doit etre non vide"
    #if len(tab) == 0:
    #    return None
    maxi = tab[0]
    for e in tab:
        if e > maxi:
            maxi = e
    return maxi


#%% Passage de paramètres

def incremente(x):
    x = x + 1
    return x
    
def incremente_tab(tab):
    for k in range(len(tab)):
        tab[k] = tab[k] + 1
        
        
a = 5
t1 = [5, 6, 7]
t2 = t1
b = incremente(a)
incremente_tab(t1)

#%% Exercice 7 instruction assert


#assert a < b, "a doit être <  à b"
#
#
#
#a, b = b, a
#
#assert a < b, "a doit être <  à b"
#Traceback (most recent call last):
#
#  File "<ipython-input-11-3ab3dd6e1909>", line 1, in <module>
#    assert a < b, "a doit être <  à b"
#
#AssertionError: a doit être <  à b


#%% Exo 7 Q1

def echange(tab, i, j):
    assert 0 <= i < len(tab) and 0 <= j < len(tab), "erreur"
    tab[i], tab[j] = tab[j], tab[i]
    #on modifie tab par effet de bord
    #pas de return la fonction renvoie None
    
t1 = [k ** 2 for k in range(11)]
t2 = [k for k in range(21) if k % 3 == 0]
echange(t1, 0, 11)
print(t1)
assert t1 == [4, 1, 0, 9, 16, 25, 36, 49, 64, 81, 100]
    

#%% Méthodes de tableau dynamique 

#Voir Cours, exemples traités en console

#%% Exercice 8

def filtre_notes(tab):
    tinf = []
    for k in range(len(tab)):
        if tab[k] < 10:
            tinf.append(tab[k])
    return tinf


def filtre_notes2(tab):
    tinf = []
    for note in tab:
        if note < 10:
            tinf.append(note)
    return tinf

def filtre_notes3(tab):
    return [note for note in tab if note < 10]

notes = [5,7,8,14,10,9,14, 7]

def maximum_tab(tab):
    """Renvoie l'élément maximum de tab"""
    assert len(tab) > 0, "tab doit etre non vide"
    #if len(tab) == 0:
    #    return None
    maxi = tab[0]
    for e in tab:
        if e > maxi:
            maxi = e
    return maxi
    
def pos_maximum_tab(tab):
    """Renvoie l'élément maximum de tab
    et la liste des positions où il est atteint
    """
    assert len(tab) > 0, "tab doit etre non vide"
    pos = []
    maxi = tab[0]
    for k in range(len(tab)):
        if tab[k] > maxi:
            maxi = tab[k]
            pos = [k]
        elif tab[k] == maxi:
            pos.append(k)
        print(tab[k], maxi, pos)
    return [maxi, pos]




