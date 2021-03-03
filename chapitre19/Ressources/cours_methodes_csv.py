# -*- coding: utf-8 -*-
"""
Exemples du cours sur les tables de données :
manipulation de fichiers CSV en Python
"""
#%% Exemple 1 : méthode classique : 

# partie 1 lecture 

f = open('clients_mini.csv', mode = 'r', encoding = 'utf8', newline='')
attributs = f.readline().rstrip().split(',')
table = [ligne.rstrip().split(',') for ligne in f]
f.close()


# partie 2 réécriture

g = open('clients_mini_copie.csv', mode = 'w', encoding = 'utf8', newline = '')
premiere_ligne = ','.join(attributs) + '\n'
g.write(premiere_ligne)
for enregistrement in table:
    g.write(','.join(enregistrement) + '\n')
g.close()


#%% Méthode 2 : avec le module csv

import csv  # import du module 

#%% Extraction sous forme de tableau de tableaux
import csv  # import du module 
f = open('clients_mini.csv', mode = 'r', encoding = 'utf8', newline = '')
reader = csv.reader(f, delimiter = ',')
table = [ligne for ligne in reader]
f.close()


#%% Extraction sous forme de tableau de dictionnaires
import csv  # import du module 

# Extraction
f = open('clients_mini.csv', mode = 'r', encoding = 'utf8', newline = '')
reader = csv.DictReader(f, delimiter = ',')  #création de l'objet reader
table = [enregistrement for enregistrement in reader]
f.close()

# Écriture d'une table sous forme de tableau de dictionnaires dans un fichier CSV

g = open('clients_mini_copie2.csv', mode = 'w', encoding = 'utf8', newline='')
attributs = list(table[0].keys())
writer = csv.DictWriter(g, delimiter = ',', fieldnames = attributs) #création de l'objet writer
writer.writeheader()   #écriture des attibuts
for enregistrement in table:
    writer.writerow(enregistrement)  #écriture des enregistrements
g.close()

