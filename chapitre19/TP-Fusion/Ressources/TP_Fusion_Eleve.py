#!/usr/bin/env python
# coding: utf-8

"""TP Tables de données, fusion
Version élève
Exécuter les cellules dans l'ordre
Compléter au niveau des balises #ELEVE : 
"""


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


#%% Exercice 1 Fusion de tables par réunion


#%% Question 3 : chargement de deux tables (prénoms à Rennes en 2011 et 2010)

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

#ELEVE : 
def reunion_table(table1, table2):
    """Paramètres : deux tables table1 et table2
    Valeur renvoyée : nouvelle table obtenue par concaténation de table1 et table2
    """
    return "à compléter"

#ELEVE : 
def prenom_max(table):
    """Paramètres : table (ou réunion de tables) de prénoms 
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
            "à compléter"
        elif histo[prenom] == effectif_max:
            "à compléter"
    return (effectif_max, tab_max)     

prenom_10_11 = reunion_table(prenom_10, prenom_11)

#ELEVE : postconditions, décommenter pour tester
# assert prenom_10_11[0] == {'ANNAISS': '2010', 'MNAISS': '', 'CODCOM': '35238', 'LBCOM': 'RENNES', 
#                            'SEXE': 'FEMME', 'PRN': 'Louise', 'NBR': '48'}
# assert prenom_10_11[len(prenom_10)] == {'ANNAISS': '2011', 'MNAISS': '', 'CODCOM': '35238', 'LBCOM': 'RENNES',
#                                         'SEXE': 'FEMME', 'PRN': 'Manon', 'NBR': '57'}
# assert len(prenom_10) + len(prenom_11) == len(prenom_10_11)


#ELEVE : compléter pour filtrer uniquement les prénoms féminins dans prenom_10_11
prenom_f_10_11 = [enreg for enreg in prenom_10_11 if "à compléter"]

#ELEVE : postconditions, décommenter pour tester
#assert prenom_max(prenom_f_10_11) == (103, ['Louise'])

#%% Question 6 :   Premier point de vigilance 

#chargement de deux nouvelles tables
prenom_08 = lecture_csv('Prénoms2008GF_Rennes.csv', ';', 'ISO8859')
prenom_09 = lecture_csv('Prénoms2009GF_Rennes.csv', ';', 'ISO8859')
prenom_08_09 = reunion_table(prenom_08, prenom_09)

def clef_prenom(enreg):
    return enreg['PRN']

def clef_prenom_annee(enreg):
    return (enreg['PRN'], enreg['ANNAISS'])

#ELEVE : Décommentez les deux instructions suivantes, quelle est celle qui échoue ? Pourquoi ? 
#assert sorted(prenom_09, key = clef_prenom_annee) == sorted(prenom_09, key = clef_prenom)
#prenom_08_09_tri = sorted(prenom_08_09, key = clef_prenom_annee) 


#%% Question 7 : Second point de vigilance 

#%% chargement de la table des prénoms en 2014
prenom_14 = lecture_csv('Prénoms2014GF_ Rennes.csv', ';', 'ISO8859')
# noter aussi l'espace malencontreux dans le nom de fichier => encore une erreur humaine

#ELEVE : sélectionner uniquement les mois de naissance en 2014
mois_14 = ["à compléter" for enreg in prenom_14]
#ELEVE : postcondition, décommenter pour tester
#assert mois_14[:4] == ['', '', '', '']

#%% chargement de la table des prénoms en 2015
prenom_15 = lecture_csv('Prénoms2015GF_Rennes.csv', ';', 'ISO8859')
#ELEVE : Décommenter la ligne suivante pour tester
#mois_15 = [enreg['MNAISS'] for enreg in prenom_15]


#ELEVE :  Réunir les tables prenom_14 et prenom_15 dans prenom_14_15
#puis trier prenom_14_15 par prenom puis année
"à compléter"


#%% Exercice 2 :  fusion de tables par jointure

#%%Question 1 Chargement des tables

films = lecture_csv('films.csv', ',', 'utf8')
realisateurs = lecture_csv('realisateurs.csv', ',', 'utf8')

#postconditions
assert films[:2] == [{'titre': 'La  vie est belle', 'réalisateur': 'Capra', 'année': '1946'},
 {'titre': 'La  vie est belle', 'réalisateur': 'Benigni', 'année': '1997'}] and len(films) == 36
assert len(realisateurs) == 22 and realisateurs[:2] == [{'nom': 'Coppola', 'prénom': 'Sofia', 'pays': 'USA'},
 {'nom': 'Coppola', 'prénom': 'Francis Ford', 'pays': 'USA'}]


#%% Question 2 : Fusion des tables par jointure

def fusion_enregistrements(f, r):
    return {'titre' : f['titre'], 'année' : f['année'], 'nom réalisateur' : r['nom'],
            'prénom réalisateur' : r['prénom'], 'pays réalisateur' : r['pays']}

#ELEVE :
def fusion_tables(films, realisateurs):
    """Fusion des tables films et réalisateurs
     par jointure sur l'attibut 'nom' du réalisateur"""
    fusion = []
    for f in films:
        for r in realisateurs:
            "à compléter"
    return fusion

#ELEVE :
def fusion_tables_comprehension(films, realisateurs):   
    return "à compléter"


jointure_f_r = fusion_tables(films, realisateurs)
jointure_f_r2 = fusion_tables_comprehension(films, realisateurs)

#ELEVE :
#postcondition, décommenter pour tester
#assert jointure_f_r == jointure_f_r2


#%% Question 3 : Première incohérence 

#ELEVE :
#décommenter pour tester
#print([enreg for enreg in jointure_f_r if enreg['titre'] == 'Lost in translation'])
#print(len(jointure_f_r), len(films))


#%% Question 4 : Seconde  incohérence 

#ELEVE :
#décommenter pour tester
#print([enreg for enreg in films if enreg['titre'] == 'Autant en emporte le vent'])
#print([enreg for enreg in jointure_f_r if enreg['titre'] == 'Autant en emporte le vent'])


#%% Question 5 :  Une solution aux incohérences précédentes :
# utiliser un identifiant unique, on reprend les jointures 

#%% Chargement des nouvelles tables
films_idr = lecture_csv('films_idr.csv', ',', 'utf8')
realisateurs_id = lecture_csv('realisateurs_id.csv', ',', 'utf8')

#ELEVE :
def fusion_tables_id(films, realisateurs):   
    return "à compléter"


jointure_f_r3 = fusion_tables_id(films_idr, realisateurs_id)


#ELEVE :
#postconditions, décommenter pour tester
#assert[enreg for enreg in jointure_f_r3 if enreg['titre'] == 'Apocalypse Now'] == [{'titre': 'Apocalypse Now',
#   'année': '1979',
#   'nom réalisateur': 'Coppola',
#   'prénom réalisateur': 'Francis Ford',
#   'pays réalisateur': 'USA'}]
#assert len(jointure_f_r3) == len(films)

