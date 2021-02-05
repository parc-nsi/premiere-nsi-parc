# -*- coding: utf-8 -*-

## Imports des modules

import re
from random import random
import matplotlib.pyplot as plt
import numpy as np


## Fonctions outils 

def  nettoyer_fichier(fichier):
    """Prend en paramètre :
    - fichier de type str qui est un chemin vers un fichier texte
    Nettoie le texte contenu dans le fichier : 
    - suppression des symboles de ponctuation
    - réduction des espaces multiples
    - conversion en minuscules
    Retourne le texte nettoyé"""
    #ouverture du fichier
    f = open(fichier, 'r')
    data = f.read()
    #suppression des symboles de ponctuation
    data = re.sub(r'[^\w\s]', ' ', data)
    #réduction des espaces multiples
    data = re.sub(r'\s+',' ', data)
    #fermeture du fichier
    f.close()  
    #conversion en minuscules
    data = data.lower()
    return data

## Exercice 1

def extraire_tab_mot(source):
    """Prend en paramètre :
    - source de type str qui est un chemin vers un fichier texte
    Nettoie le texte contenu dans le fichier avec nettoyer_fichier
    Découpe le texte selon le séparateur espace simple
    Retourne le tableau obtenu"""
    #à compléter

# assertion à vérifier
tab_mots_mousquetaires = extraire_tab_mot('3mousquetaires.txt')
assert (len(tab_mots_mousquetaires), tab_mots_mousquetaires[:3]) == (239574, ['introduction', 'il', 'y'])

def histogramme(tab):
    """Prend en paramètre:
    - un tableau de mots de type str
    Retourne un dictionnaire histo associant
    à chaque mot son nombre d'occurrences dans tab
    """
    # à compléter

# assertion à vérifier
histo_mousquetaires = histogramme(tab_mots_mousquetaires)
assert(histo_mousquetaires['milady'] == 710 \
       and histo_mousquetaires['cardinal'] == 551)

def plus_frequent_mot(histo):
    """Prend en paramètre :
    - un dictionnaire histo 
    représentant les nombres d'occurences de mots dans un texte
    Renvoie un tuple constitué du  plus grand nombre d'occurences    
    et du tableau de tous les mots atteignant ce maximum"""
    # à compléter

# assertion à vérifier
assert(plus_frequent_mot(histo_mousquetaires) == (8964, ['de']))

def tri_valeur(paire_clef_valeur):
    clef, valeur = paire_clef_valeur
    return valeur

def tri_clef(paire_clef_valeur):
    clef, valeur = paire_clef_valeur
    return clef


def top_unigramme(source, but):
    """Prend en paramètres 
    - source de type str qui est un chemin vers un fichier texte
    - but de type str qui est un chemin vers un fichier texte
    Extrait dans un tableau les mots du texte contenu dans source 
    Construit un dictionnaire représentant un histogramme de ce tableau
    Convertit ce dictionnaire en tableau et le classe par ordre décroissant des occurences
    Renvoie ce tableau classé et recopie son contenu dans le fichier but
    """
    # à compléter


# assertions à vérifier

top_mousquetaires = top_unigramme('3mousquetaires.txt', 'top-mousquetaires.csv')
assert(top_mousquetaires[:4] == [('de', 8964), ('et', 5792), ('la', 5357), ('le', 5191)])

top_swann = top_unigramme('ducotedechezswann.txt', 'top-swann.csv')
assert(top_swann[:4] == [('de', 7794), ('la', 3937), ('et', 3898), ('à', 3829)])


## Exercice 4

def prochain_histo(source):
    """Prend en paramètre :
    - source de type str qui représente un chemin vers un fichier texte
    Extrait le tableau de mots contenu dans le texte de source
    Renvoie un dictionnaire de dictionnaires prochain tel que prochain[mot1][mot2]
    représente le nombre d'occurences de mot2 juste après mot1
    telles que mot1 mot2 soit un digramme"""
    #à compléter


# assertions à vérifier
prochain_mousquetaires = prochain_histo('3mousquetaires.txt')
assert prochain_mousquetaires['pose'] == {'qui': 2, 'gracieuse': 1, 'et': 1}
assert prochain_mousquetaires['la']['bastille'] == 29
assert prochain_mousquetaires['de']['buckingham'] == 59


def somme_histo(histo):
    """Prend en paramètre :
    - histo qui est un dictionnaire de coules (mot : str, effectif : int)
    Renvoie un entier qui est  la somme des effectifs    
    """
    # à compléter

# assertions à vérifier
assert somme_histo(prochain_mousquetaires['pose']) == 4
assert somme_histo(prochain_mousquetaires['de']) == 8964


def prochain_freq(source):
    """Prend en paramètre :
    - source de type str qui représente un chemin vers un fichier texte
    Renvoie un dictionnaire de dictionnaires fred tel que fred[mot1][mot2]
    représente la fréquence de mot2 parmi les digrammes commençant par mot1
    """
    # à compléter

# assertions à vérifier
freq_digramme_mousquetaire = prochain_freq('3mousquetaires.txt')
assert freq_digramme_mousquetaire['pose']['gracieuse'] == 0.25
assert freq_digramme_mousquetaire['pose']['et'] == 0.25
assert freq_digramme_mousquetaire['pose']['qui'] == 0.5


## Exercice 5

def histo_cumul(histo):
    """Prend en paramètre :
    - histo un dictionnaire associant à un mot de type str une fréquence de type float
    Retourne un tableau de paires (mot, fréquence cumulée)
    """
    # à compléter


def mot_suivant(premier_mot, freq):
    """Prend en paramètre :
    - premier_mot de type str
    - freq un dictionnaire de dictionnaires 
    tel que freq[premier_mot] est la distribution de fréquences
    des seconds mots dans les digrammes commençant par premier_mot    
    Choisit aléatoirement puis renvoie le second mot d'un tel digramme
    """
    # à compléter

def frequence_echantillon_mot_suivant(taille, premier_mot, freq):
    """Prend en paramètre :
    - taille de type int représentant la taille de l'échantillon
    - premier_mot de type str
    - freq un dictionnaire de dictionnaires 
    tel que freq[premier_mot] est la distribution de fréquences
    des seconds mots dans les digrammes commençant par premier_mot    
    Renvoie un dictionnaire représentant la distribution de fréquences
    des seconds mots parmi les digrammes commençant par premier_mot
    sur un échantillon de taille passée en paramètre
    """
    
#module pour la gestion des chemins dans un système de fichiers
import os.path   

def autoTexte(source, debut, taille):
    freq = prochain_freq(source)
    base, ext = os.path.splitext(source)
    #nom du fichier de sortie
    sortie = '-'.join([base, 'auto', str(taille)]) + ext
    #ouverture du fichier de sortie
    f = open(sortie, 'w')
    mot = debut
    f.write(mot + ' ')
    taille_ligne = len(mot) + 1
    for k in range(taille - 1):
       #à compléter
    f.close()