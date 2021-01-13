#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:56:02 2021

@author: fjunier
"""

#%% Exercice 1
from math import sqrt

def milieu(A, B):
    """
    Parametre : A et B deux tuples de coordonnée de points (x, y)
    Renvoie les coordonnées du milieu du segment [AB]
    """
    xA, yA = A
    xB, yB = B
    return ( (xA + xB) / 2,  (yA + yB)/2 )

def distance(A, B):
    """
    Paramètres : A et B deux tuples de coordonnée de points (x, y)
    Renvoie la distance entre A et B
    """
    xA, yA = A
    xB, yB = B
    return sqrt( (xB - xA) ** 2 + (yB - yA) ** 2 )

def longueurs(A, B, C):
    """
    Parametre : A, B et C  trois tuples de coordonnée de points (x, y)
    Renvoie les coordonnées du milieu du segment [AB]
    """
    return (distance(A, B), distance(B, C), distance(C,A))