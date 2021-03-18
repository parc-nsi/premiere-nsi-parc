#!/usr/bin/env python

import csv 
from faker import Faker
from random import randint


#%% Générer un fichier CSV avec prénom,nom,moyenne
fake = Faker('fr_FR')
Faker.seed(0)   #pour générer toujours les mêmes données

RECOMPENSES = [ 'rien', 'encouragements', 'compliments', 'félicitations']

def generer_eleve():
    prenom = fake.first_name()
    nom = fake.last_name_nonbinary()
    moyenne = randint(0, 20)
    return {'prénom' : prenom, 'nom' : nom, 'moyenne' : moyenne}

def generer_table_eleves(nombre):
    return [ generer_eleve()  for _ in range(nombre)]    
    

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
    
    
if __name__ == "__main__":
    table_eleves = generer_table_eleves(500)
    ecriture_csv(table_eleves, 'eleves.csv' ,',')
#%%Extraire un tel fichier dans une table, trier cette table dans l'ordre décroissant des moyennes
#puis dans l'ordre alphabétique croissant des noms et l'ordre décroissant des moyennes 

#%% Traiter un tel fichier CSV en créant une nouvelle table avec les récompenses
# compter les récompenses
# trier les récompenses 


#table_eleves = lecture_csv('eleves.csv', ',')

    
    