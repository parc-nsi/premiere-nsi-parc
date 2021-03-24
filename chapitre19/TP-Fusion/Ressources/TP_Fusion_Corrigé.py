#!/usr/bin/env python
# coding: utf-8

#%% Import des modules et outils de lecture / écriture

import csv 


def lecture_csv(fichier, delimiteur, encodage):
    """
    Paramètre : un chemin vers un fichier CSV
    Valeur renvoyée : un tableau de dictionnaires, extraction de la table contenue dans le fichier
    """
    f = open(fichier, mode = 'r', encoding = encodage, newline='')
    reader = csv.DictReader(f, delimiter = delimiteur)  #création de l'objet reader
    table = [dict(enregistrement) for enregistrement in reader]
    f.close()
    return table

def ecriture_csv(table, fichier, delimiteur, encodage):
    """
    Paramètre : 
        un chemin vers un fichier CSV
        une table comme tableau de dictionnaires partageant les mêmes clefs, de valeurs str
    Valeur renvoyée :
        None, écrit table dans fichier avec Dictriter du  module CSV 
    """
    g = open(fichier, mode = 'w', encoding = encodage, newline='')
    attributs = list(table[0].keys())
    writer = csv.DictWriter(g, delimiter = delimiteur, fieldnames = attributs) #création de l'objet writer
    writer.writeheader()   #écriture des attibuts
    for enregistrement in table:
        writer.writerow(enregistrement)  #écriture des enregistrements
    g.close()


#%% Exercice 1 Question 3

prenom_11 = lecture_csv('Prénoms2011GF_Rennes.csv', ';', 'ISO8859')

assert prenom_11[:2] == [{'ANNAISS': '2011',
  'MNAISS': '',
  'CODCOM': '35238',
  'LBCOM': 'RENNES',
  'SEXE': 'FEMME',
  'PRN': 'Manon',
  'NBR': '57'},
 {'ANNAISS': '2011',
  'MNAISS': '',
  'CODCOM': '35238',
  'LBCOM': 'RENNES',
  'SEXE': 'FEMME',
  'PRN': 'Louise',
  'NBR': '55'}]  and len(prenom_11) == 248



prenom_10 = lecture_csv('Prénoms2010GF_Rennes.csv', ';', 'ISO8859')
assert prenom_10[:2] == [{'ANNAISS': '2010',
  'MNAISS': '',
  'CODCOM': '35238',
  'LBCOM': 'RENNES',
  'SEXE': 'FEMME',
  'PRN': 'Louise',
  'NBR': '48'},
 {'ANNAISS': '2010',
  'MNAISS': '',
  'CODCOM': '35238',
  'LBCOM': 'RENNES',
  'SEXE': 'FEMME',
  'PRN': 'Chloé',
  'NBR': '44'}] and len(prenom_10) == 221


#%% Question 5


def reunion_table(table1, table2):
    """Paramètres : deux tables table1 et table2
    Valeur renvoyée : nouvelle table obtenue par concaténation de table1 et table2
    """
    return table1 + table2


def prenom_max(table):
    """Paramètres : table de prénoms 
    Valeur renvoyée : 
        tuple constitué de l'effectif maximum
        et du tableau des prénoms  les plus fréquents
    """
    effectif_max = int(table[0]['NBR'])
    histo = {table[0]['PRN'] : effectif_max}   
    tab_max = [table[0]['PRN']]
    for enreg in table[1:]:
        prenom = enreg['PRN']
        effectif = int(enreg['NBR'])
        if prenom not in histo:
            histo[prenom] = effectif
        else:
            histo[prenom] += effectif
        if histo[prenom] > effectif_max:
            tab_max = [prenom]
            effectif_max = histo[prenom]
        elif histo[prenom] == effectif_max:
            tab_max.append(prenom)
    return (effectif_max, tab_max)            



prenom_10_11 = reunion_table(prenom_10, prenom_11)

#postconditions, décommenter pour tester
assert prenom_10_11[0] == {'ANNAISS': '2010', 'MNAISS': '', 'CODCOM': '35238', 'LBCOM': 'RENNES', 
                           'SEXE': 'FEMME', 'PRN': 'Louise', 'NBR': '48'}
assert prenom_10_11[len(prenom_10)] == {'ANNAISS': '2011', 'MNAISS': '', 'CODCOM': '35238', 'LBCOM': 'RENNES',
                                        'SEXE': 'FEMME', 'PRN': 'Manon', 'NBR': '57'}
assert len(prenom_10) + len(prenom_11) == len(prenom_10_11)

prenom_f_10_11 = [enreg for enreg in prenom_10_11 if enreg['SEXE'] == 'FEMME']

assert prenom_max(prenom_f_10_11) == (103, ['Louise'])




#%% Question 6 :  Premier problème : même nombre d'attributs des tables fusionnées mais les noms des attibuts ont changé
# 
# Le fichier 'Prénoms2008GF_Rennes.csv' est le seul où l'attribut d'année de naissance est nommé ANNEE_NAISSANCE au lieu de ANNAISS


prenom_08 = lecture_csv('Prénoms2008GF_Rennes.csv', ';', 'ISO8859')
prenom_09 = lecture_csv('Prénoms2009GF_Rennes.csv', ';', 'ISO8859')
prenom_08_09 = reunion_table(prenom_08, prenom_09)

def clef_prenom(enreg):
    return enreg['PRN']

def clef_prenom_annee(enreg):
    return (enreg['PRN'], enreg['ANNAISS'])


#%% Postcondition sans problème
assert sorted(prenom_09, key = clef_prenom_annee) == sorted(prenom_09, key = clef_prenom)

#%% Postcondition similaire qui pose problème
# l'attribut 'ANNAISS' de la table prenom_09
# a changé de nom en 'ANNEE_NAISSANCE' dans la table prenom_08 => exemple d'incohérence
assert sorted(prenom_08, key = clef_prenom_annee) == sorted(prenom_08, key = clef_prenom)

sorted(prenom_08_09, key = clef_prenom_annee)



#%% Question 7  Second point de vigilance : le nombre d'attributs a changé
# 
# Pour Prénoms2015GF_Rennes.csv  l'attribut MNAISS a été supprimé,
# Il n'était pas utilisé dans les autres fichiers.
# Comme les enregistrements sont des dictionnaires, 
# cela ne pose pas de problème d'accès aux autres attributs (pas de décalage d'index).

#%%

prenom_14 = lecture_csv('Prénoms2014GF_ Rennes.csv', ';', 'ISO8859')
# noter aussi l'espace malencontreux dans le nom de fichier => encore une erreur humaine
mois_14 = [enreg['MNAISS'] for enreg in prenom_14]
assert mois_14[:4] == ['', '', '', '']

#%%
prenom_15 = lecture_csv('Prénoms2015GF_Rennes.csv', ';', 'ISO8859')
mois_15 = [enreg['MNAISS'] for enreg in prenom_15]
prenom_14_15 = reunion_table(prenom_14, prenom_15)


sorted(prenom_14_15, key = clef_prenom_annee)[:3]


# Exercice 2 : Fusion de tables par jointure
#%% Question 1

films = lecture_csv('films.csv', ',', 'utf8')
realisateurs = lecture_csv('realisateurs.csv', ',', 'utf8')


assert films[:2] == [{'titre': 'La  vie est belle', 'réalisateur': 'Capra', 'année': '1946'},
 {'titre': 'La  vie est belle', 'réalisateur': 'Benigni', 'année': '1997'}] and len(films) == 36
assert len(realisateurs) == 22 and realisateurs[:2] == [{'nom': 'Coppola', 'prénom': 'Sofia', 'pays': 'USA'},
 {'nom': 'Coppola', 'prénom': 'Francis Ford', 'pays': 'USA'}]


#%% Question 2

def fusion_enregistrements(f, r):
    return {'titre' : f['titre'], 'année' : f['année'], 'nom réalisateur' : r['nom'],
            'prénom réalisateur' : r['prénom'], 'pays réalisateur' : r['pays']}

def fusion_tables(films, realisateurs):
    fusion = []
    for f in films:
        for r in realisateurs:
            if f['réalisateur'] == r['nom']:
                fusion.append(fusion_enregistrements(f, r))
    return fusion

def fusion_tables2(films, realisateurs):   
    return [fusion_enregistrements(f, r) for f in films for r in realisateurs if f['réalisateur'] == r['nom']]


jointure_f_r = fusion_tables(films, realisateurs)
jointure_f_r2 = fusion_tables2(films, realisateurs)
assert jointure_f_r == jointure_f_r2

## Question 3
#%% Premier problème d'incohérence : trois réalisateurs pour le même film ! Le nom du réalisateur ne permet pas de l'identitifier de façon unique, même si on rajoutait le prénom on pourrait peut être tomber sur des cas d'homonymie 

print([enreg for enreg in jointure_f_r if enreg['titre'] == 'Lost in translation'])
print(len(jointure_f_r), len(films))

## Question 4 
#%% Second problème d'incohérence : 
# #'Autant en emporte le vent' n'a pas retrouvé son réalisateur
# #à cause d'une erreur de saisie dans la table 'films.csv'  
# #où 'Flemming' a été écrit avec deux m au lieu de 1 !

print([enreg for enreg in jointure_f_r if enreg['titre'] == 'Autant en emporte le vent'])


#Question 5 Une solution aux problèmes d'incohérences : 
# #utiliser un identifiant unique, on reprend les jointures 

films_idr = lecture_csv('films_idr.csv', ',', 'utf8')
realisateurs_id = lecture_csv('realisateurs_id.csv', ',', 'utf8')

def fusion_tables3(films, realisateurs):   
    return [fusion_enregistrements(f, r) for f in films for r in realisateurs if f['idr'] == r['id']]


#Plus de problème d'incohérence, chaque film retrouve son réalisateur grace à l'identifiant unique !
jointure_f_r3 = fusion_tables3(films_idr, realisateurs_id)
assert[enreg for enreg in jointure_f_r3 if enreg['titre'] == 'Apocalypse Now'] == [{'titre': 'Apocalypse Now',
  'année': '1979',
  'nom réalisateur': 'Coppola',
  'prénom réalisateur': 'Francis Ford',
  'pays réalisateur': 'USA'}]
assert len(jointure_f_r3) == len(films)