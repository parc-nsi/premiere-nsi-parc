# -*- coding: utf-8 -*-
"""
Corrigés des exercices du cours 
sur l'indexation et la recherche dans une table
"""

#%% Exercice 2
import re 

NBJOURS_MOIS = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31],
           [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]]

DEPARTEMENTS = [str(k).zfill(2) for k in range(1, 96)] + ['971', '972', '973', '974', '975', '2A', '2B']


def valide_email(email):
    # Expression régulière pour valider un email 
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
    return re.search(regex,email) is not None

def valide_departement(departement):
    return departement in DEPARTEMENTS

def bissextile(a):
    return a % 400= 0 or (a % 100 != 0 and a % 4 == 0)

def annee_valide(j):
    return 1920 <= int(j) <= 2005

def mois_valide(m):
    return 1 <= int(m) <= 12

def jour_valide(a, m, j):
    return (bissextile(int(a)) and  1 <= int(j) <= NBJOURS_MOIS[0][int(m)]) or 1 <= int(j) <= NBJOURS_MOIS[1][int(m)]

def valide_anniversaire(date):
    a, m, j = date.split('-')
    return  annee_valide(a) and mois_valide(m) and jour_valide(j)
