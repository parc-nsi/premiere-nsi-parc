#!/usr/bin/env python

"""Consigne : compléter au niveau des  à "compléter"
les fonctions :
    
    1)  moyenne_table
    2) enreg_avec_recompense
    3)  generer_table_recompenses
    4) decompte_recompenses
    5) clef_tri_moyenne_decroissant
    6) clef_tri_alphabetique_croissant_moyenne_decroissant
    
    Chaque fonction est accompagné d'un test unitaire => pour tester, 
    désactiver les commentaires dans le programme principal à partir de la ligne 151
    Pour les tris il faut aussi compléter le programme principal en lignes 167 et 171
"""

import csv

#Import / Export d'un tel fichier CSV ver la représentation d'une tble en Python (tableau de dictionnaires)
def lecture_csv(fichier, delimiteur):
    """
    Paramètre : un chemin vers un fichier CSV
    Valeur renvoyée : un tableau de dictionnaires, extraction de la table contenue dans le fichier
    """
    f = open(fichier, mode = 'r', encoding = 'utf8', newline='')
    reader = csv.DictReader(f, delimiter = delimiteur)  #création de l'objet reader
    table = [dict(enregistrement) for enregistrement in reader]
    f.close()
    return table

def ecriture_csv(table, fichier, delimiteur):
    """
    Paramètre : 
        un chemin vers un fichier CSV
        une table comme tableau de dictionnaires partageant les mêmes clefs, de valeurs str
    Valeur renvoyée :
        None, écrit table dans fichier avec Dictriter du  module CSV 
    """
    g = open(fichier, mode = 'w', encoding = 'utf8', newline='')
    attributs = list(table[0].keys())
    writer = csv.DictWriter(g, delimiter = delimiteur, fieldnames = attributs) #création de l'objet writer
    writer.writeheader()   #écriture des attibuts
    for enregistrement in table:
        writer.writerow(enregistrement)  #écriture des enregistrements
    g.close()
    
def moyenne_table(table_eleves) :
    """Paramètre : table_eleves est une représentation de la table extraite de eleves.csv
        sous forme de tableau de dictionnaires. Attention les attributs 'moyenne' sont de 
        type 'str'
    Valeur renvoyée : un flottant représentant la moyenne de tous les élèves
    de la table arrondie à 2 chiffres après la virgule
    """
    somme = 0
    compteur = 0
    for enreg in table_eleves:
        "à compléter"
        "à compléter"
    return round(somme / compteur, 2)

def test_moyenne_table():
    assert moyenne_table(table_eleves) == 11.46
    print("Test unitaire de moyenne_table réussi")
    
def enreg_avec_recompense(enreg):
    """
    Paramètre : enreg un dictionnaire de clefs 'prénom', 'nom', 'moyenne' 
                Attention toutes les clefs ont des valeurs de type str
    Valeur renvoyée : extension du dictionnaire avec une nouvelle clef
    'récompense' de valeurs s :
            'insuffisant' si moyenne < 8
            'médiocre' si 8 <= moyenne < 10
            'passable' si 10 <= moyenne < 12
            'encouragements' si  12 <= moyenne < 14
            'compliments' si   14 <= moyenne < 16
            'félicitations' si moyenne > 16
    """
    copie = { clef : valeur for clef, valeur in enreg.items() }
    m = "à compléter"
    if m < 8:
        copie['récompense'] = 'insuffisant'
    elif "à compléter":
        copie['récompense'] = 'médiocre'
    elif "à compléter":
        copie['récompense'] = 'passable'
    elif "à compléter":
        copie['récompense'] = 'encouragements'
    elif "à compléter":
        copie['récompense'] = 'compliments'
    else:
        copie['récompense'] = 'félicitations'
    return copie


def generer_table_recompenses(table_eleves):
    """Paramètre : table_eleves est une représentation de la table extraite de eleves.csv
        sous forme de tableau de dictionnaires
    Valeur renvoyée : une extension de table_eleves avec un nouvel attribut 'récompense'
    chaque nouvel enregistrement est généré par enreg_avec_recompense
    """
    table_recompenses = "à compléter"  
    return table_recompenses

def test_generer_table_recompenses():
    """Test unitaires de generer_table_recompenses"""
    table_recompenses = generer_table_recompenses(table_eleves)
    assert table_recompenses[0] == {'prénom': 'Zoé', 'nom': 'Collin',
                                    'moyenne': '19', 'récompense': 'félicitations'}
    assert table_recompenses[8] == {'prénom': 'Roland', 'nom': 'Joly', 
                                    'moyenne': '8', 'récompense': 'médiocre'}
    print("Test unitaires de generer_table_recompenses réussis")
    
def decompte_recompenses(table_recompenses):
    """Paramètre : table_recompenses  est une représentation de la table renvoyée 
                    par generer_table_recompenses. 
    Valeur renvoyée : un dictionnaire avec le décompte de chaque récompense
    """
    decompte = dict()
    for enreg in table_recompenses:
        "à compléter"
        "à compléter"
        "à compléter"
        "à compléter"
    return decompte

def test_decompte_recompenses():
    """Test unitaires de decompte_recompenses"""
    decompte = decompte_recompenses(table_recompenses)
    assert decompte == {'félicitations': 89,
                         'médiocre': 77,
                         'compliments': 95,
                         'insuffisant': 86,
                         'passable': 81,
                         'encouragements': 72}
    print("Test unitaires de decompte_recompenses réussis")
    
    
     
def clef_tri_moyenne_decroissant(enreg):
    """Clef de tri par moyenne décroissante
    Attention la valeur de l'attribut 'moyenne' de enreg est de type str"""
    return "à compléter"

def clef_tri_alphabetique_croissant_moyenne_decroissant(enreg):
    """Clef de tri par moyenne décroissante
    Attention la valeur de l'attribut 'moyenne' de enreg est de type str"""
    return "à compléter"
    

#Programme principal
table_eleves = lecture_csv('eleves.csv', ',')
#Décommenter lorsque moyenne_table est complétée
#test_moyenne_table()

#Décommenter lorsque generer_table_recompenses est complétée
#table_recompenses = generer_table_recompenses(table_eleves)
#test_generer_table_recompenses()

#Décommenter lorsque decompte_recompenses est complétée
#test_decompte_recompenses()

#Décommenter e lorsque clef_tri_moyenne_decroissant terminée
#table_recompenses = generer_table_recompenses(table_eleves)

#Ecrire une instruction qui permet de trier  table_recompenses dans l'ordre décroissant des moyennes
#table_tri1 = "à compléter"

#Ecrire une instruction qui permet de trier  table_recompenses :
#d'abord dans l'ordre alphabétique croissant puis dans l'ordre décroissant des moyennes
#table_tri2 = "à compléter"