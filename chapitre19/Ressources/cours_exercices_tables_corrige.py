# -*- coding: utf-8 -*-
"""
Corrigés des exercices du cours 
sur l'indexation et la recherche dans une table
"""
import re    #module pour traiter des expressions régulières
import csv   #module pour traiter les fichiers CSV


#%% Exercice 2


#nombre de jours par mois
NBJOURS_MOIS = {'normale' : [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31],
                'bissextile' : [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31] }

DEPARTEMENTS = [str(k).zfill(2) for k in range(1, 96)] + ['971', '972', '973', '974', '975', '2A', '2B']


# Fonctions de lecture / écriture dans un fichier CSV


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

# Fonctions de validation des données

def valide_email(email):
    """
    Parammètre : email de type str
    Valeur renvoyée : booléen indiquant si email de format valide
    """
    # Expression régulière pour valider un email 
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
    return re.search(regex,email) is not None

def valide_departement(departement):
    return departement in DEPARTEMENTS

def valide_visites(visites):
    return int(visites) >= 0

def valide_depenses(depenses):
    return float(depenses) >= 0

def bissextile(a):
    """
    Paramètre : a de type int représentant une année
    Valeur renvoyée  : booléen indiquant si l'année est bissextile
    """
    return a % 400 == 0 or (a % 100 != 0 and a % 4 == 0)

def valide_annee(j):
    return 1920 <= j <= 2005

def valide_mois(m):
    """
    Paramètre : m de type int représentant un mois
    Valeur renvoyée  : booléen indiquant si le mois est valide (entre 1 et 12)
    """
    return 1 <= m <= 12

def valide_jour(a, m, j):
    """
    Paramètre : a, m, j de type int représentant l'année, le mois et le jour
    Valeur renvoyée  : booléen indiquant si le jour est valide pour l'année et le mois donnés
    """
    return (bissextile(a) and   1 <= j <= NBJOURS_MOIS['bissextile'][m]) or 1 <= j <= NBJOURS_MOIS['normale'][m]

def valide_naissance(date):
    """
    Paramètre : date de type str au format 'année-mois-jour', ex: '2002-01-07'
    Valeur renvoyée  : booléen indiquant si le jour est valide pour l'année et le mois donnés
    """
    a, m, j = date.split('-')
    return  valide_annee(int(a)) and valide_mois(int(m)) and valide_jour(int(a), int(m), int(j))

def valide_enregistrement(enreg):
    """
    Paramètre : un enregistrement de type dictionnaire
    Valeur renvoyée  : booléen indiquant si toutes les valeurs des attibuts sont valides
    """
    return  valide_departement(enreg['département']) and valide_naissance(enreg['naissance']) \
        and valide_visites(enreg['visites']) and valide_depenses(enreg['dépenses']) and valide_email(enreg['email'])


# Fonctions de conversion d'enregistrement 

def conversion_vers_table(enregistrement):
    """
    Paramètre : un enregistrement de type dictionnaire
    Valeur renvoyée  : un enregistrement de type dictionnaire avec conversion des valeurs dans le type cible
    """
    return { 'nom' : enregistrement['nom'],
            'prénom'  : enregistrement['prénom'],
            'email' : enregistrement['email'],
            'département' : enregistrement['département'],
            'naissance' : enregistrement['naissance'],
            'visites' : int(enregistrement['visites']),
            'dépenses' : float(enregistrement['dépenses'])
            }

def conversion_vers_fichier(enregistrement):
    """
    Paramètre : un enregistrement de type dictionnaire
    Valeur renvoyée  : un enregistrement de type dictionnaire avec conversion des valeurs dans le type str
    """
    return { 'nom' : enregistrement['nom'],
            'prénom'  : enregistrement['prénom'],
            'email' : enregistrement['email'],
            'département' : enregistrement['département'],
            'naissance' : enregistrement['naissance'],
            'visites' : str(enregistrement['visites']),
            'dépenses' : str(enregistrement['dépenses'])
            }


def main():
    """Code client"""
    #Traitement / validation / filtrage
    table = lecture_csv('clients_avec_erreurs.csv',',')
    table_valide = [conversion_vers_table(enregistrement) for enregistrement in table if valide_enregistrement(enregistrement)]
    # postconditions / tests
    assert len(table) == 1000 and len(table_valide) == 635
    assert table_valide[0] == {'nom': 'Bailly', 'prénom': 'Aurélie', 'email': 'abailly1@gmail.com', 
                               'département': '22', 'naissance': '1986-09-22',
                               'visites': 54, 'dépenses': 2397.57}
    table_valide_str = [conversion_vers_fichier(enregistrement) for enregistrement in table_valide]
     #écriture de la table validée
    ecriture_csv(table_valide_str, 'clients_sans_erreurs.csv', ',')
   

# code client
if __name__ == "__main__":
    "décommentez pour exécuter le code client"
    main()
